import json, os, re
import streamlit as st

st.set_page_config(page_title="Ubiquitous | Resume Match Assistant", page_icon="✦", layout="wide")
st.markdown("""
<style>
.main {background:#f7f5f1}
.block-container {max-width:1120px;padding-top:2rem}
.hero {padding:1.4rem 1.8rem;border-radius:20px;background:#171717;color:white;margin-bottom:1.2rem}
.hero p {color:#dedbd4}
div[data-testid="stMetric"] {background:white;padding:18px;border:1px solid #e8e2d9;border-radius:16px}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>✦ Resume–Job Match Assistant</h1><p>Evidence-based resume feedback using a transparent scoring rubric.</p></div>', unsafe_allow_html=True)

def words(s):
    return set(re.findall(r"[a-zA-Z][a-zA-Z+#.]*", s.lower()))

SKILLS = ["python","java","c++","sql","machine learning","deep learning","nlp","computer vision","fastapi","flask","react","docker","aws","azure","git","pandas","numpy","tensorflow","pytorch","excel","communication","data analysis","statistics","power bi","tableau"]
def analyze(resume, jd):
    if len(resume.strip()) < 30 or len(jd.strip()) < 30:
        return {"status":"insufficient_input","match_score":0,"category_scores":{},"gaps":["Provide a resume and a job description of at least 30 characters."],"strengths":[],"rewritten_bullets":[],"next_steps":["Add complete, non-placeholder input."],"limitations":["Insufficient input; no fit score was calculated."]}
    rlow, jlow = resume.lower(), jd.lower()
    required = [s for s in SKILLS if s in jlow]
    matched = [s for s in required if s in rlow]
    missing = [s for s in required if s not in rlow]
    skill_score = round(40 * len(matched) / max(1,len(required))) if required else 20
    project_terms = ["project","developed","built","implemented","experience","intern","work"]
    exp_hits = sum(1 for t in project_terms if t in rlow and t in jlow)
    exp_score = min(30, round(30*exp_hits/ max(1, min(4,len(project_terms)))))
    jd_terms = [w for w in words(jd) if len(w)>4]
    keyword_hits = sum(1 for w in jd_terms if w in words(resume))
    keyword_score = min(20, round(20*keyword_hits/max(1,len(jd_terms))))
    clarity_score = 7 if len(resume.split()) >= 60 else 5
    total = skill_score+exp_score+keyword_score+clarity_score
    strengths = ["Evidence found for: "+", ".join(matched)] if matched else ["No listed technical skills matched the detected job requirements."]
    next_steps = ["Add truthful evidence for "+s+" if you have it." for s in missing[:5]]
    if not next_steps: next_steps=["Tailor project bullets to the responsibilities in the job description."]
    return {"status":"assessed","match_score":total,"category_scores":{
        "skills":{"score":skill_score,"out_of":40,"reason":f"{len(matched)} of {len(required)} detected skills found."},
        "experience_projects":{"score":exp_score,"out_of":30,"reason":"Heuristic overlap of experience/project evidence terms; manual review is recommended."},
        "keywords":{"score":keyword_score,"out_of":20,"reason":f"{keyword_hits} of {len(jd_terms)} longer job-description terms overlap."},
        "clarity":{"score":clarity_score,"out_of":10,"reason":"Basic length-based proxy; not a full writing-quality model."}},
        "gaps":missing,"strengths":strengths,"rewritten_bullets":[],
        "next_steps":next_steps,"limitations":["Local demo uses transparent lexical heuristics, not an LLM or trained predictive model.","Scores are indicative and do not predict hiring outcomes. Review all feedback manually."]}

with st.sidebar:
    st.subheader("About this prototype")
    st.write("Prompt-engineering workflow prototype for resume/JD comparison.")
    st.caption("The local demo mode uses deterministic heuristics. For real LLM prompt execution, connect a provider and validate outputs.")
    st.markdown("**Rubric**")
    st.write("Skills 40 · Experience/projects 30 · Keywords 20 · Clarity 10")
    st.markdown("**Prompt versions**")
    st.write("v1 Baseline · v2 Expanded rubric · v3 Evidence-constrained JSON")

c1,c2=st.columns(2)
with c1:
    resume=st.text_area("RESUME",height=300,placeholder="Paste anonymised resume text here…")
with c2:
    jd=st.text_area("JOB DESCRIPTION",height=300,placeholder="Paste job description here…")
if st.button("Analyze match",type="primary",use_container_width=True):
    result=analyze(resume,jd)
    st.session_state["last_result"]=result
    st.session_state["last_inputs"]={"resume":resume,"job_description":jd}
if "last_result" in st.session_state:
    result=st.session_state["last_result"]
    st.divider()
    if result["status"]=="assessed":
        st.metric("Indicative match score",f'{result["match_score"]}/100')
        cols=st.columns(4)
        for col,(key,label) in zip(cols,[("skills","Skills"),("experience_projects","Experience/projects"),("keywords","Keywords"),("clarity","Clarity")]):
            col.metric(label,f'{result["category_scores"][key]["score"]}/{result["category_scores"][key]["out_of"]}')
            col.caption(result["category_scores"][key]["reason"])
    else:
        st.warning("Insufficient input")
    a,b,c=st.columns(3)
    with a:
        st.subheader("Strengths")
        for x in result["strengths"]: st.write("✓ "+x)
    with b:
        st.subheader("Gaps")
        for x in result["gaps"]: st.write("• "+x)
    with c:
        st.subheader("Next steps")
        for x in result["next_steps"]: st.write("→ "+x)
    st.subheader("Limitations")
    for x in result["limitations"]: st.caption("ℹ "+x)
    st.download_button("Download analysis JSON",json.dumps(result,indent=2),file_name="resume_match_result.json",mime="application/json")
st.caption("Prototype for educational evaluation. Do not upload sensitive personal data. This score is not a hiring probability.")

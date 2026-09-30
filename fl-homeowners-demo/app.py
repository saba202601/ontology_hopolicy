import json
from pathlib import Path
import streamlit as st
from model import hurricane_deductible, letter

ROOT=Path(__file__).parent
D=json.loads((ROOT/'data/demo.json').read_text())
st.set_page_config(page_title='Florida homeowners ontology',page_icon='🏠',layout='wide')
st.title('Florida homeowners policy')
st.caption('An ontology demonstration connecting policy facts, coverage questions and client communication.')
st.info('Fictional HO-3 style example. No carrier policy was supplied. Figures are assumptions, not a quote or coverage decision.')
with st.sidebar:
    st.header('Policy assumptions')
    dwelling=st.number_input('Dwelling limit ($)',min_value=1000,value=400000,step=10000)
    rate=st.selectbox('Illustrated hurricane deductible',options=[0.02,0.05,0.10],format_func=lambda x:f'{x:.0%}')
    aop=st.number_input('All-other-perils deductible ($)',min_value=0,value=2500,step=500)
    st.caption('These options illustrate scenarios; availability depends on the policy.')
tabs=st.tabs(['Policy','Ontology','Deductible scenario','Client letter','Sources'])
with tabs[0]:
    st.subheader(D['policy_id'])
    st.write(f"{D['homeowner']} · {D['property']}")
    rows=[dict(c) for c in D['coverage']]
    rows[0]['limit']=dwelling
    st.dataframe(rows,hide_index=True,width='stretch')
    st.caption('Only Coverage A changes with the sidebar input. B–F remain independently selected example limits.')
    st.subheader('Questions for the policy review')
    for item in D['review_items']: st.write('• '+item)
with tabs[1]:
    st.graphviz_chart('digraph { rankdir=LR; Policy -> Homeowner [label="hasInsured"]; Policy -> Property [label="insures"]; Policy -> Coverage [label="hasCoverage"]; Policy -> Deductible [label="hasDeductible"]; ClaimScenario -> Peril [label="causedBy"]; Deductible -> Peril [label="appliesTo"]; ReviewItem -> Source [label="supportedBy"]; }')
    st.dataframe(D['classes'],hide_index=True,width='stretch')
    st.dataframe(D['relations'],hide_index=True,width='stretch')
    st.download_button('Download OWL / Turtle ontology',(ROOT/'data/ontology.ttl').read_bytes(),'ontology.ttl')
with tabs[2]:
    st.write('Assumes a covered hurricane wind loss on one dwelling. Flood, multiple structures, insurer changes and settlement adjustments are outside this calculator.')
    subsequent=st.checkbox('Subsequent hurricane, same calendar year and insurer group')
    credit=st.number_input('Insurer-confirmed prior deductible credit ($)',min_value=0,max_value=int(dwelling*rate),value=0,disabled=not subsequent)
    loss=st.number_input('Hypothetical covered loss below the policy limit ($)',min_value=0,max_value=dwelling,value=min(30000,dwelling),step=1000)
    deductible=hurricane_deductible(dwelling,rate,aop,credit if subsequent else 0,subsequent)
    cols=st.columns(3)
    cols[0].metric('Applicable deductible',f'${deductible:,.0f}')
    cols[1].metric('Loss less deductible',f'${max(0,loss-deductible):,.0f}')
    cols[2].metric('Deductible absorbed by loss',f'${min(loss,deductible):,.0f}')
    st.caption('Arithmetic illustration only. It does not calculate an insurer payment or apply depreciation, sublimits, exclusions or other settlement conditions.')
with tabs[3]:
    text=letter(D,dwelling,rate,aop)
    st.text(text)
    st.download_button('Download client letter',text,'client-letter.txt')
with tabs[4]:
    for s in D['sources']: st.markdown(f"[{s['title']}]({s['url']}) — accessed {s['accessed']}")
    st.caption('Source guidance supports the concepts. All policy amounts and personal details are fictional. Workbook edits do not synchronize with the app; JSON is the app source.')

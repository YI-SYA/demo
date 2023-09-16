import streamlit as st




st.set_page_config(page_title="Yi SYA galery", page_icon='👨‍🔧')

st.write("<h1 style='font-size: 36px;'>### 👨‍🔧 Welcome !!!!</h1>", unsafe_allow_html=True)

st.image("https://img.freepik.com/free-vector/illustration-data-analysis-graph_53876-18131.jpg?w=1060&t=st=1694825221~exp=1694825821~hmac=7be6aa9b22465a49079e1f5d527196edd0f9e259c463f33f431268cb141bf48a")

st.info("My [Github](https://github.com/YI-SYA)")

st.markdown("---")


st.write("""
## 📄 My Name is Muhyiddin Syarif


## <a>I am Data Scientist from Indonesia</a>

---

## 👨‍🎓 Taking the course

####

##### 👥 2023 Cohort

* **Start**: 16 January 2023 (Monday) at 18:00 CET
* **Registration link**: https://airtable.com/shr6oVXeQvSI5HuWD
* Subscribe to our [public Google Calendar](https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) (it works from Desktop only)
* [Cohort folder](cohorts/2023/) with homeworks and deadlines""", unsafe_allow_html=True)

st.error("2023 Cohort ended in the 18th May of 2023. To see 2023 cohort ressources see this [link](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2023).")

st.markdown("""
##### 👨‍🔧 Self-paced mode

All the materials of the course are freely available, so that you can take the course at your own pace

* Follow the suggested syllabus (see below) week by week
* You don't need to fill in the registration form. Just start watching the videos and join Slack
* Check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) if you have problems
* If you can't find a solution to your problem in FAQ, ask for help in Slack

---

### 📓 Prerequisites

To get the most out of this course, you should feel comfortable with coding and command line
and know the basics of SQL. Prior experience with Python will be helpful, but you can pick
Python relatively fast if you have experience with other programming languages.

Prior experience with data engineering is not required.

---

### 👨‍🏫 Instructors

- [Ankush Khanna](https://linkedin.com/in/ankushkhanna2)
- [Sejal Vaidya](https://linkedin.com/in/vaidyasejal)
- [Victoria Perez Mola](https://www.linkedin.com/in/victoriaperezmola/)
- [Kalise Richmond](https://www.linkedin.com/in/kaliserichmond/)
- [Jeff Hale](https://www.linkedin.com/in/-jeffhale/)
- [Alexey Grigorev](https://linkedin.com/in/agrigorev)

---

### ❔ Asking for help in Slack

The best way to get support is to use [DataTalks.Club's Slack](https://datatalks.club/slack.html). Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel.

To make discussions in Slack more organized:

* Follow [these recommendations](asking-questions.md) when asking for help
* Read the [DataTalks.Club community guidelines](https://datatalks.club/slack/guidelines.html)

---

### 💌 Supporters and partners

Thanks to the course sponsors for making it possible to create this course

<a href="https://www.prefect.io/">
    <img height="100" style="margin-right: 4rem;" src="https://github.com/DataTalksClub/mlops-zoomcamp/raw/main/images/prefect.png">
</a>

<a href="https://www.piperider.io/">
    <img height="130" src="https://github.com/DataTalksClub/data-engineering-zoomcamp/raw/main/images/piperider.png">
</a>

#
Do you want to support our course and our community? Please reach out to [alexey@datatalks.club](alexey@datatalks.club)
            
---
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>

If you liked the project please leave a star. 
            
##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral) 

""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

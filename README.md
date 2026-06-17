"# intelligence-task-manager" 

 

בפניכם מערכת לניהול יחידה מודעינית הכוללת נתונים של סוכנים ומשימות:

המערכת נועדה לניהול משימות לפי רמה של המשימה כמו כן לניהול סוכנים, סמכות הסוכן וסטטוס התקדמות המשימה

agents:

אפשרויות:

יצירת סוכן חדש
הצגת כל הסוכנים הקיימים
הצגת סוכן ספציפי לפי id
עדכון כללי של סוכן
הצגת משימות,כמות,כמות שבוצעו או נכשלו ואחוזי הצלחה במשימות




missions:

אפשרויות:

יצירת משימה חדשה
הצגת כל המשימות הקיימות
הצגת משימה ספציפי לפי id
הצגה לפי סטטוס
ספירת משימות פתוחות /קריטיות
הצגת סוכן עם החוזי הצלחה הגבוה




מבנה התקיות:


intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
│
├──models/
│ ├──agent_model.py
│ ├──mission_model.py
│
│
├──utils/
│ ├──agent_logic.py
│ ├──mission_logic.py
│
│
├── README.md
├── requirements.txt
└── .gitignore



מבנה הטבלאות:

agents:

| id | name | specialty | is_active | completed_Missions | failed_missions | agent_rank |




missions:

| id | title | description | location | difficulty | importance | status | risk_level | assigned_agent_id |


מחלקות:

DB_connection:

מחלקה אחראית על החיבור עם הנתונים

get_connection() -> מחזירה חיבור ל MySQL

create_database() -> מייצר database במידה ולא קיים רצה בעת עליית המערכת

create_tables() -> מייצרת את הטבלאות (agents,missions) במידה ולא קיים רצה בעת עליית המרכת


AgentDb:

מחלקת האחראית על כל הפעולות מול הטבלה agents

create_agent(data) -> יוצרת סוכן חדש ומחזירה אותו

get_all_agents() -> מחזירה רשימת הסוכנים

get_agent_by_id(id) -> מחזירה סוכן ספציפי לפי id

update_agent(id,data) -> מעדכנת כל השדות של הסוכן למעט id מחזירה האם הפעולה הצליחה

desactive_agent(id) -> השבתת סוכן מחזירה האם הפעולה הצליחה

increment_completed(id) -> מעדכנת מספר משימות שהצליחו מחזירה האם הפעולה הצליחה

increment_failed(id) -> מעדכנת מספר משימות שנכשלו  מחזירה האם הפעולה הצליחה

get_agent_performance(id) -> מחזירה דוח מילון עם סה"כ משימות, משימות שהצליחו, משימות שנכשלו ואחוזי ההצלחה של המשימות

count_active_agents() -> מחזירה מספר הסוכנים הפעילים




missions:

מחלקה האחראית על כל הפעולות מול טבלת missions

create_mission(data) -> יוצרת משימה חדש ומחזירה אותה

get_all_missions() -> מחזירה רשימת המשימות

get_mission_by_id(id) -> מחזירה משימה ספציפית לפי id

assing_mission(m_id,a_id) -> משייכת משימה לסוכן מחזירה האם הפעולה הצליחה

update_mission_status(id,status) -> משנה את סטטטוס המשימה מחזירה האם הפעולה הצליחה

get_open_mission_by_id(id) ->  מחזירה את המשימות ( ASSIGNED/IN_PROGRESS) של הסוכן

count_all_mission() -> סה"כ משימות

count_by_status(status) -> ספירה לפי סטטוס

count_by_open_missions() -> ספירה לפי משימות פתוחות

count_critical_missions() -> ספירה לפי קריטי

get_top_agent() -> הסוכן עם הכי הרבה משימות מוצלחות


חוקי המערכת:

דרגת הסוכן חייבת ליהות אחד מ  Commander / Senior / Junior

difficulty ו-importance חייבים להיות בין 1 ל10- — אחרת שגיאה

risk_level מתעדכן אטומטית על ידי המערכת 

רק סוכן פעיל יכול לקבל משימה

סוכן לא יכול להחזיק יותר מ 3 משימות פתוחות( ASSIGNED/IN_PROGRESS)

משימה עם דרגת סיכון קריטי יכולה להתבצע רק על ידי commander

ניתן לשייך רק משימה חדשה(new) לאחר שיוך מתעדכן ל assigned

כמו כן ניתן רק להתחיל משימה משוייכת לאחר מתעדכן ל in progress

ניתן לסיים משימה רק אחרי שהסטטוס שלה היא in progress  ולשנות ל falied/completed

ביטול המשימה ניתן רק בסטטוס new/assigned




הוראות הרצה לדוקר:

פקודה:
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0


לינק לרפוסיטורי:
https://github.com/mordechaigoldfeld-svg/intelligence-task-manager


ספריות הנדרשות להרצת הפרוייקט נמצאות ב:

requirements.txt

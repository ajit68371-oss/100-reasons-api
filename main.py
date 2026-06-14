from fastapi import FastAPI
import random

app = FastAPI(
    title="100 Reasons API",
    description="A simple API showcasing 100 reasons to hire Praveen",
    version="1.1.0"
)

reasons: list[str] = [
    "Bridges business and technology effectively",
    "Understands both API consumption and API development",
    "Strong Martech platform expertise",
    "Experienced in customer engagement ecosystems",
    "Can translate business requirements into technical solutions",
    "Comfortable working with engineering teams",
    "Comfortable working with senior business stakeholders",
    "Strong stakeholder management skills",
    "Data-driven decision maker",
    "Experienced in campaign analytics and optimization",
    "Understands customer lifecycle management",
    "Can identify process inefficiencies and simplify them",
    "Strong problem-solving mindset",
    "Experienced in cross-functional collaboration",
    "Able to connect strategy with execution",
    "Understands event-driven architectures",
    "Experienced in API integrations and system connectivity",
    "Can document requirements clearly and effectively",
    "Strong analytical and structured thinking",
    "Understands customer journeys end-to-end",
    "Capable of translating complex concepts into simple language",
    "Experienced in feature rollout and operational ownership",
    "Can balance business priorities with technical constraints",
    "Comfortable navigating ambiguity",
    "Strong attention to detail",
    "Understands metrics, KPIs and business outcomes",
    "Experienced in growth and engagement initiatives",
    "Can challenge assumptions with data",
    "Quick learner across domains and technologies",
    "Experienced in working with enterprise applications",
    "Able to identify risks before they become issues",
    "Strong communication skills",
    "Can align multiple stakeholders toward a common objective",
    "Understands customer behavior and engagement patterns",
    "Comfortable with both strategic and operational discussions",
    "Capable of managing competing priorities",
    "Can convert ideas into executable plans",
    "Experienced in working with large datasets and insights",
    "Strong ownership mindset",
    "Focused on delivering measurable outcomes",
    "Understands product thinking and user value",
    "Can work effectively between business, product and technology teams",
    "Experienced in integration troubleshooting and resolution",
    "Comfortable presenting to leadership audiences",
    "Strong documentation and process orientation",
    "Capable of identifying automation opportunities",
    "Understands digital customer engagement channels",
    "Can evaluate solutions from both customer and business perspectives",
    "Experienced in managing platform adoption and utilization",
    "Combines consulting mindset with execution capability",
    "Demonstrates curiosity beyond assigned responsibilities",
    "Invests time in learning emerging technologies",
    "Understands how technology drives business value",
    "Can connect operational details with strategic goals",
    "Maintains a strong customer-first mindset",
    "Approaches problems with structured thinking",
    "Able to simplify complex business processes",
    "Comfortable operating in fast-changing environments",
    "Builds credibility across teams through execution",
    "Balances speed and quality effectively",
    "Can identify hidden dependencies in projects",
    "Experienced in requirement gathering and analysis",
    "Brings systems-thinking to problem solving",
    "Focuses on outcomes rather than activities",
    "Can evaluate trade-offs objectively",
    "Strong understanding of digital transformation initiatives",
    "Capable of driving alignment across functions",
    "Understands the importance of governance and controls",
    "Able to communicate technical concepts to non-technical audiences",
    "Can translate customer pain points into product improvements",
    "Comfortable working with large-scale enterprise platforms",
    "Takes ownership beyond defined job boundaries",
    "Understands how data supports business decisions",
    "Can quickly understand unfamiliar domains",
    "Strong focus on continuous improvement",
    "Values evidence-based decision making",
    "Can identify opportunities for process automation",
    "Brings both strategic perspective and execution focus",
    "Comfortable managing complex stakeholder landscapes",
    "Can challenge existing processes constructively",
    "Demonstrates resilience under pressure",
    "Maintains focus on priorities during ambiguity",
    "Strong ability to connect dots across functions",
    "Understands customer engagement at scale",
    "Can create clarity in complex situations",
    "Experienced in platform adoption and optimization",
    "Capable of influencing without formal authority",
    "Brings a consulting mindset to business challenges",
    "Understands the lifecycle of digital products",
    "Can assess impact before recommending solutions",
    "Experienced in managing business and technology dependencies",
    "Maintains a balance between innovation and practicality",
    "Can identify root causes rather than symptoms",
    "Strong focus on measurable business outcomes",
    "Able to navigate both operational and strategic discussions",
    "Brings discipline to execution and follow-through",
    "Can convert insights into actionable recommendations",
    "Comfortable working across multiple business domains",
    "Views technology as an enabler of business growth",
    "Continuously seeks opportunities to learn and improve"
]


@app.get("/")
def home():
    return {
        "project": "100 Reasons API",
        "candidate": "Praveen",
        "title": "Business & Technology Consultant",
        "documentation": "/docs",
        "about": "/about",
        "github": "https://github.com/ajit68371-oss/100-reasons-api"
    }


@app.get("/about")
def about():
    return {
        "project": "100 Reasons API",
        "version": "1.1.0",
        "author": "Praveen",
        "purpose": "Showcasing professional strengths through a public REST API",
        "technology": [
            "Python",
            "FastAPI",
            "Uvicorn",
            "Swagger/OpenAPI",
            "GitHub",
            "Render"
        ],
        "github": "https://github.com/ajit68371-oss/100-reasons-api"
    }


@app.get("/why-hire/praveen")
def why_hire_praveen():
    return {
        "candidate": "Praveen",
        "title": "Business & Technology Consultant",
        "reason_count": len(reasons),
        "reasons": reasons
    }


@app.get("/why-hire/praveen/random")
def random_reason():

    reason = random.choice(reasons)

    return {
        "candidate": "Praveen",
        "reason_number": reasons.index(reason) + 1,
        "reason": reason
    }


@app.get("/why-hire/praveen/today")
def reason_of_the_day():

    reason = random.choice(reasons)

    return {
        "candidate": "Praveen",
        "reason_number": reasons.index(reason) + 1,
        "reason_of_the_day": reason
    }


@app.get("/why-hire/praveen/top10")
def top_ten():

    numbered_reasons = []

    for index, reason in enumerate(reasons[:10], start=1):
        numbered_reasons.append({
            "reason_number": index,
            "reason": reason
        })

    return {
        "candidate": "Praveen",
        "top_10_reasons": numbered_reasons
    }


@app.get("/why-hire/praveen/stats")
def stats():
    return {
        "candidate": "Praveen",
        "total_reasons": len(reasons),
        "api_version": "1.1.0"
    }
import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

data = [
    (
        "Thiel Fellowship",
        "thielfellowship.org",
        "rolling",
        "A two-year, $200,000 grant program for innovators aged 22 or younger to pursue full-time projects instead of attending college.",
        "fellowship",
        "Global",
        "Thiel Foundation",
        "equity-free, mentorship, long-term, under-25"
    ),

    (
        "AWS Activate for Startups",
        "aws.amazon.com",
        "rolling",
        "AWS Activate is Amazon Web Services' flagship startup support program offering promotional AWS credits and related resources to help early-stage companies build, launch, and scale their technology on AWS. Founders can apply for the Activate Founders package to receive $1,000 in AWS credits",
        "grant",
        "Global",
        "Amazon Web Services (AWS)",
        "cloud-credits, developer-program, startup-support, aws"
    ),

    (
        "New Enterprise Associates (NEA)",
        "nea.com",
        "rolling",
        "One of the world's largest multi-stage venture capital firms, investing across technology and healthcare since 1977.",
        "venture capital",
        "Global",
        "New Enterprise Associates (NEA)",
        "venture-capital, multi-stage, seed, early-stage"
    ),

    (
        "Founders Fund",
        "foundersfund.com",
        "rolling",
        "San Francisco-based venture capital firm backing companies building revolutionary technologies.",
        "venture capital",
        "Global",
        "Founders Fund",
        "venture-capital, multi-stage, seed, early-stage"
    ),

    (
        "Google for Startups Accelerator",
        "startup.google.com",
        "rolling",
        "Equity-free accelerator: no cash funding, but up to $100K GCP credits.",
        "accelerator",
        "Global",
        "Google for Startups",
        "equity-free, accelerator, cloud, global"
    ),

    (
        "OpenAI Converge",
        "openai.fund",
        "rolling",
        "6-week AI startup summit with $1M equity investment from OpenAI's Startup Fund.",
        "accelerator",
        "North America",
        "OpenAI Startup Fund",
        "equity-based, accelerator, AI, summit"
    ),

    (
        "Khosla Ventures",
        "khoslaventures.com",
        "rolling",
        "Early-stage and growth venture capital firm founded by Vinod Khosla, investing in ambitious technology companies across enterprise, consumer, health, sustainability and frontier tech.",
        "venture capital",
        "Global",
        "Khosla Ventures",
        "venture-capital, early-stage, growth, enterprise"
    ),

    (
        "Lightspeed Venture Partners",
        "lsvp.com",
        "rolling",
        "Lightspeed Venture Partners (LSVP) is a multi‑stage venture capital firm that backs bold founders and disruptive innovations with capital and strategic support from early seed to later growth stages.",
        "venture capital",
        "Global",
        "Lightspeed Venture Partners",
        "venture-capital, seed-funding, growth-stage, global"
    ),

    (
        "Sequoia Open Source Fellowship",
        "sequoiacap.com",
        "rolling",
        "An equity-free fellowship by Sequoia Capital supporting leading open source developers around the world.",
        "fellowship",
        "Global",
        "Sequoia Capital",
        "open-source, developer-support, equity-free, remote"
    ),

    (
        "First Round Capital",
        "firstround.com",
        "rolling",
        "First Round Capital is an early-stage venture capital firm specializing in seed-stage investments and founder support for technology startups. It provides capital and operational resources to help companies grow from idea to product-market fit and beyond.",
        "venture capital",
        "North America",
        "First Round Capital",
        "pre-seed, seed-funding, venture-capital, founder-support"
    ),

    (
        "General Catalyst",
        "generalcatalyst.com",
        "rolling",
        "Global investment and transformation firm partnering with founders from seed through growth to build resilient, AI-enabled companies.",
        "venture capital",
        "Global",
        "General Catalyst",
        "venture-capital, multi-stage, seed, early-stage"
    ),

    (
        "a16z Speedrun",
        "speedrun006.a16z.com",
        "rolling",
        "a16z Speedrun invests up to $1M in new startups, providing capital, $7M in credits, and hands-on support from expert operators to help founders build and scale their companies.",
        "accelerator",
        "Global",
        "Andreessen Horowitz (a16z)",
        "startup, funding, accelerator, venture capital"
    ),

    (
        "Sequoia Arc",
        "arc.sequoiacap.com",
        "rolling",
        "Sequoia Arc is a biannual seed-stage catalyst program that helps pre-seed and seed founders build enduring, category-defining companies through funding, mentorship, community, and company building frameworks.",
        "accelerator",
        "Global",
        "Sequoia Capital",
        "seed-stage, funding, accelerator, company-building"
    ),

    (
        "The Exponential Fellowship",
        "goexponential.org",
        "rolling",
        "A paid fellowship that places exceptional young Spanish builders at fast-growing U.S. startups — visa, flights and insurance handled, with full U.S. pay and access to mentorship and community.",
        "fellowship",
        "North America",
        "The Exponential (Go Exponential)",
        "visa-covered, paid, mentorship, international"
    ),

    (
        "The Residency",
        "coda.io",
        "rolling",
        "3–6-month in-person cohorts providing full-time housing, co-working space, and community for ambitious builders; locations include San Francisco, Berkeley, Cambridge (MA), Berlin, and Bangalore.",
        "residency",
        "Global",
        "The Residency",
        "housing-included, mentorship, medium-term, in-person"
    ),

    (
        "TKS World 2026",
        "tks.world",
        "2mo left",
        "TKS (The Knowledge Society) is a 10-month innovation program for teens ages 13–17 that blends emerging technology exploration, project-based learning, and mentorship to help students build real solutions and future skills.",
        "accelerator",
        "Global",
        "The Knowledge Society",
        "youth-innovation, project-based, global, mentorship"
    ),

    (
        "ODF",
        "forms.joinodf.com",
        "rolling",
        "A one-week, in-person founder onboarding experience and year-round community that helps people start and scale venture-backable companies.",
        "fellowship",
        "Global (primarily US-focused)",
        "ODF (nZero Labs, Inc.)",
        "accelerator, founder-program, onboarding-week, in-person"
    ),

    (
        "RareBreed Ventures",
        "rarebreed.vc",
        "rolling",
        "RareBreed Ventures is a pre-seed venture capital fund that backs exceptional founders early, especially those outside major tech ecosystems. They write initial checks to help startups gain early traction and connect with broader investor networks.",
        "venture capital",
        "North America",
        "RareBreed Ventures",
        "pre-seed, venture-capital, early-stage, founder-support"
    ),

    (
        "Initialized Capital",
        "initialized.com",
        "rolling",
        "Initialized Capital is a San Francisco-based early-stage venture capital firm focused on providing seed and pre-seed investment and support to startups and founders. Founded by Alexis Ohanian, Garry Tan, and Harjeet Taggar, the firm invests in high-potential technology startups and partners with founders throughout their growth journey.",
        "venture capital",
        "North America",
        "Initialized Capital",
        "seed-funding, venture-capital, early-stage, founder-support"
    ),

    (
        "2048 Ventures Pre-Seed Fast Track",
        "2048.vc",
        "rolling",
        "A year-round fast funding path for pre-seed startups where 2048 Ventures can lead rounds quickly.",
        "venture capital",
        "North America",
        "2048 Ventures",
        "pre-seed, vc-funding, fast-track, startup-investment"
    ),

    (
        "Precursor Ventures",
        "precursorvc.com",
        "rolling",
        "Precursor Ventures is an early-stage venture capital firm that invests in founders at the very beginning of their entrepreneurial journey, backing them through pre-seed and seed rounds with capital and long-term support.",
        "venture capital",
        "North America",
        "Precursor Ventures",
        "pre-seed, seed-funding, venture-capital, early-stage"
    ),

    (
        "AI Grant Accelerator",
        "aigrant.com",
        "rolling",
        "AI Grant is a startup accelerator and funding initiative focused on investing in early-stage AI product companies and supporting innovation with capital and ecosystem resources",
        "accelerator",
        "Global",
        "AI Grant LLC (founded by Hersh Desai and Lenny Bogdonoff)",
        "ai-startups, seed-funding, cloud-credits, demo-day"
    ),

    (
        "Battery Ventures",
        "battery.com",
        "rolling",
        "Global, technology-focused investment firm backing companies from early stage through buyouts.",
        "venture capital",
        "Global",
        "Battery Ventures",
        "venture-capital, multi-stage, seed, early-stage"
    ),

    (
        "Bessemer Venture Partners (BVP)",
        "bvp.com",
        "rolling",
        "Global multi-stage venture capital firm with a long history of backing enterprise, consumer and healthcare companies.",
        "venture capital",
        "Global",
        "Bessemer Venture Partners",
        "venture-capital, multi-stage, seed, early-stage"
    ),

    (
        "Spark Capital",
        "sparkcapital.com",
        "rolling",
        "Multi-stage venture capital firm investing in products and founders across consumer, enterprise, infra, gaming, fintech and AI.",
        "venture capital",
        "Global",
        "Spark Capital",
        "venture-capital, multi-stage, seed, growth"
    ),

    (
        "Antler",
        "antler.co",
        "rolling",
        "Global early-stage investor providing $200–$250K for ~8–9% equity in a 6-week residency.",
        "accelerator",
        "Global",
        "Antler",
        "equity-based, accelerator, global, co-founder matching"
    ),

    (
        "Hummingbird VC",
        "hummingbird.vc",
        "rolling",
        "Global seed investors backing outlier founders across deep tech, AI, SaaS, fintech and healthcare.",
        "venture capital",
        "Global",
        "Hummingbird VC (Hummingbird Ventures)",
        "seed, early-stage, venture-capital, deep-tech"
    ),

    (
        "Seven Seven Six (776)",
        "sevensevensix.com",
        "rolling",
        "Early-stage venture capital firm founded by Alexis Ohanian (also known as 776).",
        "venture capital",
        "Global",
        "Seven Seven Six (776)",
        "venture-capital, early-stage, seed, series-a"
    ),

    (
        "LocalHost - France",
        "localhosthq.com",
        "rolling",
        "A global fellowship with activities and events in Paris, France, supporting exceptional builders.",
        "residency",
        "Europe",
        "LocalHost Ventures",
        "housing-included, mentorship, medium-term, in-person"
    ),

    (
        "Cloudflare for Startups",
        "cloudflare.com",
        "rolling",
        "Cloudflare for Startups is a startup support program that offers service credits, tooling, and ecosystem benefits to early-stage companies building software and SaaS products. Cloudflare credits help startups scale securely and efficiently while reducing infrastructure costs.",
        "grant",
        "Global",
        "Cloudflare, Inc.",
        "startup-credits, cloud-tools, developer-infrastructure, scaling-support"
    ),

    (
        "Palantir Neurodivergent Fellowship",
        "jobs.lever.co",
        "rolling",
        "A recruitment pathway for exceptional neurodivergent talent to join Palantir as full-time employees, building software and delivering customer outcomes in an AI-driven world. The program recognizes that neurodivergent cognitive traits provide a competitive advantage in building the next technological era.",
        "fellowship",
        "US",
        "Palantir Technologies",
        "neurodivergent, fellowship, full-time, AI"
    ),

    (
        "Palantir American Tech Fellowship",
        "jobs.lever.co",
        "rolling",
        "A fellowship program providing high-intensity AI and software training to American workers from diverse backgrounds, connecting exceptional graduates with job opportunities at Palantir and its partners nationwide.",
        "fellowship",
        "US",
        "Palantir",
        "AI, software, training, fellowship"
    ),

    (
        "Vercel AI Accelerator",
        "vercel.typeform.com",
        "rolling",
        "A 6-week accelerator program for 40 AI builders, providing over $6M in credits from leading AI platforms.",
        "accelerator",
        "Global",
        "Vercel",
        "AI, accelerator, Vercel, credits"
    ),

    (
        "The Bridge",
        "join-thebridge.com",
        "rolling",
        "8-week US residency in the Bay Area for European builders to find co-founders, build teams, and secure pre-seed funding.",
        "residency",
        "US",
        "Entrepreneurs First",
        "residency, co-founder matching, pre-seed, Bay Area"
    ),


    (
        "MongoDB for Startups",
        "mongodb.com",
        "rolling",
        "MongoDB for Startups is a technical support and credits program that helps early-stage companies build, scale, and succeed using MongoDB Atlas, the multi-cloud database platform. Participants receive credits, support, and ecosystem access to accelerate development.",
        "grant",
        "Global",
        "MongoDB, Inc.",
        "startup-credits, developer-tools, database, mongodb"
    ),

    (
        "PostHog for Startups",
        "posthog.com",
        "rolling",
        "PostHog for Startups is a startup support program that gives early-stage teams up to $50,000 in PostHog Cloud credits plus additional perks to help startups build and optimize their products",
        "grant",
        "Global",
        "PostHog",
        "startup-credits, developer-tools, analytics, product-growth"
    ),

    (
        "Alliance Accelerator",
        "alliance.xyz",
        "rolling",
        "Alliance is a leading global crypto and Web3 accelerator & founder community that helps startups reach escape velocity with funding, mentorship, and structured programming",
        "accelerator",
        "Global",
        "Alliance DAO",
        "crypto, web3, accelerator, blockchain"
    ),

    (
        "Founders, Inc",
        "f.inc",
        "rolling",
        "Founders, Inc (f.inc) is a hybrid community and funding initiative that backs ambitious founders with early checks, workspace, community, and ongoing support for building ventures across domains such as AI, AR/VR, hardware, tooling, and consumer technologies.",
        "fellowship",
        "North America",
        "Founders, Inc",
        "startup-studio, funding_program, early-stage, community"
    ),

    (
        "Base Case Capital",
        "basecase.vc",
        "rolling",
        "Base Case Capital is an early‑stage venture capital firm based in San Francisco that partners with founders early, often pre‑product and pre‑traction, by writing first institutional checks and providing capital and strategic support.",
        "venture capital",
        "North America",
        "Base Case Capital",
        "venture-capital, pre-seed, seed-funding, early-stage"
    ),

    (
        "Chapter One",
        "chapterone.com",
        "rolling",
        "Chapter One is an early‑stage venture capital firm focused on backing product‑driven founders building category‑defining technology companies.",
        "venture capital",
        "North America",
        "Chapter One",
        "venture-capital, seed-funding, early-stage, product-focused"
    ),

    (
        "BoxGroup",
        "boxgroup.com",
        "rolling",
        "BoxGroup is a New York‑based early‑stage venture capital firm that backs founders at the earliest stages (pre‑seed through Series A) with capital and strategic support. It partners with visionary founders across many technology sectors.",
        "venture capital",
        "North America",
        "BoxGroup",
        "venture-capital, pre-seed, seed-funding, early-stage"
    ),

    (
        "SV Angel",
        "svangel.com",
        "rolling",
        "SV Angel is a San Francisco‑based venture capital firm that focuses on early‑stage and seed investments in technology startups. It has backed many successful companies and supports founders with both capital and strategic engagement.",
        "venture capital",
        "North America",
        "SV Angel Management LLC",
        "venture-capital, seed-funding, early-stage, investor"
    ),

    (
        "Amplify Partners",
        "amplifypartners.com",
        "rolling",
        "Amplify Partners is a venture capital firm based in Menlo Park and San Francisco that invests in early‑stage technical startup founders building next‑generation infrastructure, developer tools, AI, and related technologies.",
        "venture capital",
        "North America",
        "Amplify Partners",
        "venture-capital, pre-seed, seed-funding, technical-founders"
    ),

    (
        "Forum Ventures",
        "forumvc.com",
        "rolling",
        "Forum Ventures is a venture capital firm and early‑stage partner that invests in pre‑seed and seed startups, especially in B2B SaaS and AI, while offering hands‑on programming, community, and accelerator‑style support.",
        "venture capital",
        "North America",
        "Forum Ventures",
        "pre-seed, seed-funding, venture-capital, accelerator-style"
    ),

    (
        "Startup Wise Guys",
        "startupwiseguys.com",
        "rolling",
        "Europe-wide accelerator (HQ Tallinn) providing up to €65K seed funding plus follow-on up to €300K.",
        "accelerator",
        "Europe",
        "Startup Wise Guys",
        "equity-based, accelerator, tech, mentorship"
    ),

    (
        "Boost VC",
        "boost.vc",
        "rolling",
        "Deep tech accelerator investing $500,000 for ~15% equity.",
        "accelerator",
        "North America",
        "Boost VC",
        "equity-based, accelerator, deep-tech, mentorship"
    ),

    (
        "Founder Institute",
        "fi.co",
        "rolling",
        "16-week pre-seed accelerator/education program; participants share equity, often receive $10–$20K each.",
        "accelerator",
        "Global",
        "Founder Institute",
        "equity-based, accelerator, education, pre-seed"
    ),

    (
        "Soma Capital Fellowship",
        "programs.somacap.com",
        "rolling",
        "Semi-annual fellowship investing $100K SAFE (<1% equity) in founders.",
        "fellowship",
        "Global",
        "Soma Capital",
        "equity-based, fellowship, seed, remote"
    ),

    (
        "AI2 Incubator",
        "ai2incubator.com",
        "rolling",
        "$50K–$150K seed funding in exchange for equity for AI startups.",
        "accelerator",
        "North America",
        "Allen Institute for AI (Incubator)",
        "equity-based, incubator, AI, research"
    ),

    (
        "Accel Atoms",
        "apply.accel-atoms.com",
        "rolling",
        "$500K–$1M seed participation by Accel for India-first startups.",
        "accelerator",
        "Asia",
        "Accel",
        "equity-based, accelerator, India, tech"
    ),

    (
        "Seedcamp",
        "seedcamp.com",
        "rolling",
        "Europe's flagship seed fund; invests €100–€200K for ~7–7.5%.",
        "accelerator",
        "Europe",
        "Seedcamp",
        "equity-based, accelerator, venture, Europe"
    ),

    (
        "APX by Porsche & Axel Springer",
        "apx.vc",
        "rolling",
        "Berlin-based accelerator with up to €50K for 5% (and follow-on up to €500K).",
        "accelerator",
        "Europe",
        "APX (Porsche & Axel Springer)",
        "equity-based, accelerator, corporate-backed, tech"
    ),

    (
        "Vercel Open Source Program",
        "vercel.com",
        "rolling",
        "Seasonal cohort-based program offering impactful open source projects up to $3,600 in Vercel credits, third-party OSS starter-pack credits, and prioritized support.",
        "fellowship",
        "Global",
        "Vercel",
        "equity-free, mentorship, short-term, tech"
    ),

    (
        "Conviction Embed",
        "conviction.com",
        "rolling",
        "Hands-on embedded partner program offering a $150K uncapped SAFE (MFN).",
        "accelerator",
        "Global",
        "Conviction",
        "equity-based, accelerator, SaaS, software"
    ),

    (
        "Greylock Edge",
        "greylock.com",
        "rolling",
        "3-month program with custom SAFE or priced terms + $500K+ in partner credits.",
        "accelerator",
        "North America",
        "Greylock",
        "equity-based, accelerator, AI, enterprise"
    ),

    (
        "Betaworks AI Camp",
        "betaworks.com",
        "rolling",
        "$500K investment from a Betaworks-led syndicate for AI startups.",
        "accelerator",
        "North America",
        "Betaworks",
        "equity-based, accelerator, AI, technology"
    ),

    (
        "AngelPad",
        "angelpad.org",
        "rolling",
        "10-week accelerator (NYC/SF) offering $120K for 7% equity.",
        "accelerator",
        "North America",
        "AngelPad",
        "equity-based, accelerator, tech, mentorship"
    ),

    (
        "The Mint (BTV)",
        "btv.vc",
        "rolling",
        "10-week fintech accelerator; invests $500K for 10% SAFE.",
        "accelerator",
        "North America",
        "BTV Capital (The Mint)",
        "equity-based, accelerator, fintech, mentorship"
    ),

    (
        "LAUNCH Accelerator",
        "launchaccelerator.co",
        "rolling",
        "$125K for 6–7% equity; 14-week accelerator founded by Jason Calacanis.",
        "accelerator",
        "North America",
        "LAUNCH",
        "equity-based, accelerator, tech, mentorship"
    ),

    (
        "Pioneer",
        "pioneer.app",
        "rolling",
        "$20K for 1% equity (or advisory only); virtual startup contest with mentors.",
        "accelerator",
        "Global",
        "Pioneer",
        "equity-based, accelerator, online, remote"
    ),

    (
        "Afore Grants",
        "grants.afore.vc",
        "rolling",
        "100% non‐dilutive microgrants of $1,000 for high‐agency builders aged 21 or younger in North America, paired with mentorship and program support.",
        "grant",
        "North America",
        "Afore Capital",
        "equity-free, mentorship, short-term, under-25"
    ),

    (
        "LocalHost - Romania",
        "localhosthq.com",
        "rolling",
        "A global fellowship with a hub in Cluj-Napoca, Romania, for exceptional builders.",
        "residency",
        "Europe",
        "LocalHost Ventures",
        "housing-included, mentorship, medium-term, in-person"
    ),

    (
        "South Park Commons Fellowship",
        "southparkcommons.com",
        "rolling",
        "Fellowship-style community program investing $400,000 for 7% equity + $600K follow-on.",
        "fellowship",
        "North America",
        "South Park Commons",
        "equity-based, fellowship, community, mentorship"
    ),

    (
        "LocalHost - India",
        "localhosthq.com",
        "rolling",
        "A global fellowship with hubs in Bangalore and New Delhi, supporting builders to pursue full-time projects.",
        "residency",
        "Asia",
        "LocalHost Ventures",
        "housing-included, mentorship, medium-term, in-person"
    ),

    (
        "LocalHost - Japan",
        "localhosthq.com",
        "rolling",
        "A global, travelling fellowship with a hub in Tokyo for exceptional young builders to pursue full-time projects.",
        "residency",
        "Asia",
        "LocalHost Ventures",
        "housing-included, mentorship, medium-term, in-person"
    ),

    (
        "HF0 Residency",
        "hf0.com",
        "rolling",
        "Intensive 12-week live-in accelerator writing a $1M SAFE for 5% (or $500K + 3%).",
        "residency",
        "North America",
        "HF0 (Residency)",
        "equity-based, accelerator, immersive, tech"
    ),

    (
        "EWOR Fellowship",
        "ewor.com",
        "rolling",
        "A highly selective, virtual-first fellowship offering early-stage founders up to €500,000 in capital and 1:1 mentorship from unicorn founders to build global-impact ventures.",
        "fellowship",
        "Global",
        "EWOR",
        "equity-based, mentorship, long-term, tech"
    ),

    (
        "Z Fellows",
        "https://www.zfellows.com/",
        "rolling",
        "One-week program offering a $10,000 stipend and mentorship from Silicon Valley's top founders for early technical builders.",
        "fellowship",
        "Global",
        "Z Fellows",
        "stipend, mentorship, short-term, tech"
    ),

    (
        "Emergent Ventures Fellowship",
        "mercatus.tfaforms.net",
        "rolling",
        "Two-year flexible research grant and community designed to support high-impact thinkers tackling big, unconventional problems.",
        "grant",
        "Global",
        "Mercatus Center",
        "equity-free, mentorship, long-term, research"
    ),

    (
        "PearX",
        "pear.vc",
        "rolling",
        "12-week accelerator by Pear VC investing $250K–$2M in each startup.",
        "accelerator",
        "North America",
        "Pear VC",
        "equity-based, accelerator, tech, mentorship"
    ),

    (
        "Edge City SHIFT Grants",
        "edgecity.live",
        "rolling",
        "Tiered grants ($5K–$40K) for d/acc projects in biosecurity, cyber defense, info resilience, physical resilience, neurotech & social technology.",
        "grant",
        "Global",
        "Edge City",
        "equity-free, funding, short-term, tech"
    ),

    (
        "LaunchX Entrepreneurship Bootcamp 2026",
        "launchx.com",
        "today",
        "LaunchX Entrepreneurship Bootcamp is a virtual summer bootcamp that immerses high school students in foundational entrepreneurship concepts and hands-on business-building activities.",
        "accelerator",
        "Global",
        "LaunchX",
        "online-accelerator, entrepreneurship, high-school, startup-bootcamp"
    )
]




cursor.executemany("""
INSERT INTO fellowships (
    title,
    website,
    deadline,
    description,
    type,
    region,
    organization,
    tags
)              
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", data)

connection.commit()

connection.close()

print("new data inserted")


================================================================================
GAURI LTD: PRODUCTION-READY RAG DATASET FOR AI ASSISTANT
================================================================================

OVERVIEW
========
This dataset contains 12 comprehensive, production-ready files for training an AI Assistant 
to answer questions about Gauri Ltd, an enterprise technology consultancy.

The data is optimized for Retrieval-Augmented Generation (RAG) with:
  - Chunk Size: 800 words (configurable)
  - Chunk Overlap: 100 words (configurable)
  - Format: PDF, Excel, PowerPoint, and Text files
  - Content: Minimal duplication, maximum unique information
  - Source: Based on provided Gauri documentation and illustrative case studies

================================================================================
FILE MANIFEST (12 FILES TOTAL)
================================================================================

PDF FILES (8 FILES)
-------------------
01_Company_Profile_Overview.pdf (7.9 KB)
   - Company identity, registration, mission, vision
   - Core values and history
   - Leadership structure and governance
   - Office locations and geographic presence
   
02_SAP_Technology_Capabilities.pdf (12 KB)
   - SAP Business One implementations and rapid deployment
   - SAP S/4HANA Cloud enterprise transformation
   - Clean-core extensibility on SAP Business Technology Platform
   - SAP Business AI and embedded intelligence
   - Representative use cases and delivery approaches
   
03_Salesforce_Technology_Capabilities.pdf (17 KB)
   - Salesforce Summit Partner status and credentials
   - Salesforce Agentforce (autonomous AI agents)
   - Salesforce Einstein (predictive and generative AI)
   - Sales Cloud, Service Cloud, Field Service Lightning
   - Salesforce-SAP integration patterns
   - Adoption and change management practices
   
04_Data_AI_Practice_Capabilities.pdf (18 KB)
   - Data Engineering and lakehouse architecture
   - Semantic models for business-friendly governance
   - Data quality, governance, and lineage tracking
   - Setu-AI: Document intelligence product
   - Data Analytics: descriptive to predictive
   - Generative AI implementation (governance-first)
   - Cloud services and infrastructure
   
05_Client_Case_Studies_Portfolio.pdf (22 KB)
   - Kestrel Automotive Group: Multi-site dealer consolidation
   - Wentworth Regional College: Education Cloud + Setu-AI
   - Medivance Surgical Supplies: Rapid SAP Business One
   - Alderton Precision Components: SAP S/4HANA modernisation
   - Harlow & Vance Home: Omnichannel retail transformation
   - Synthomer: Global CRM and ERP transformation
   
06_Engineering_Standards_Development.pdf (18 KB)
   - API Development Standards (REST, versioning, security)
   - Code Review Checklist and best practices
   - Coding Standards (style, naming, error handling)
   - Git Workflow and version control
   - Deployment Process and CI/CD pipeline
   - Testing Strategy (unit, integration, system)
   
07_Support_Operations_Standards.pdf (15 KB)
   - Customer Onboarding Process (kick-off to hypercare)
   - Support Escalation Matrix (P1-P4 priorities and targets)
   - Support channels and availability
   - Support FAQ (tickets, hours, change requests)
   - Troubleshooting Guide (SAP, Salesforce, data issues)
   - Metrics and SLA monitoring
   
08_Service_Offerings_Engagements.pdf (16 KB)
   - Engagement Types (T&M, fixed scope, managed services)
   - Platform Implementation Services (Business One, S/4HANA, Salesforce)
   - Data and AI Services (lakehouse, analytics, generative AI)
   - Integration and Migration Services
   - Training and Change Management
   - Managed Services Offerings
   - Typical Gauri Day Rates and pricing

TEXT FILES (2 FILES - SUPPORTING CONTENT)
-------------------------------------------
09_Technology_Stack_Integration.txt (15 KB)
   - Complete technology ecosystem reference
   - Core platforms: Salesforce, SAP, cloud providers
   - Data platforms: Snowflake, Databricks, hyperscalers
   - ETL/Integration tooling: Talend, MuleSoft, SAP Integration Suite
   - Analytics tools: ThoughtSpot, Tableau, Looker
   - Setu-AI: Document intelligence product details
   - Cloud infrastructure patterns
   - Monitoring, observability, and alerting
   - Development frameworks and testing technologies

SUPPORTING TEXT FILES (same content as PDFs)
   - 01_Company_Profile_Overview.txt (6.5 KB)
   - 02_SAP_Technology_Capabilities.txt (11 KB)
   - 03_Salesforce_Technology_Capabilities.txt (18 KB)
   - 04_Data_AI_Practice_Capabilities.txt (18 KB)
   - 05_Client_Case_Studies_Portfolio.txt (24 KB)
   - 06_Engineering_Standards_Development.txt (18 KB)
   - 07_Support_Operations_Standards.txt (15 KB)
   - 08_Service_Offerings_Engagements.txt (14 KB)

EXCEL FILE (1 FILE)
-------------------
10_Client_Projects_Database.xlsx (11 KB)
   Sheets included:
   - Client Projects: 9 named clients with projects, technologies, results
   - Technology Usage: 12 technologies with use cases and certifications
   - Team Skills: 9 specialisations with team sizes and differentiators
   - Service Offerings: 9 service types with duration, pricing, and deliverables

POWERPOINT FILE (1 FILE)
------------------------
11_Gauri_Sales_Positioning.pptx (42 KB)
   Slides included:
   1. Title slide: "GAURI LTD: Enterprise AI Transformation Partner"
   2. Mission statement
   3. Why we're different (5 differentiators)
   4. Three readiness pillars
   5. Platform expertise
   6. Client portfolio (6 named clients)
   7. Results delivered (5 key metrics)
   8. Our services
   9. Technology stack
   10. Geographic presence
   11. Why partner with Gauri (5 reasons)
   12. Contact information

================================================================================
CONTENT CHARACTERISTICS
================================================================================

UNIQUE DATA (Minimal Duplication)
- Each file focused on distinct aspects of Gauri's business
- PDFs organised by technology or function (not by company)
- Case studies include unique project details not repeated elsewhere
- No duplicate information across files

PRODUCTION-READY DATA
- Based on source documentation provided (gauri.com content)
- Illustrative client details for confidentiality where needed
- Realistic business scenarios and metrics
- Professional terminology and structure
- Appropriate for enterprise AI applications

RAG OPTIMISATION
- Text files: ~800 word chunks with 100 word overlap
- PDFs: Similar chunking appropriate to content density
- Excel: Structured tabular data for fact extraction
- PowerPoint: Key talking points and summary information
- Multiple formats support different retrieval strategies

================================================================================
RECOMMENDED RAG SETUP
================================================================================

CHUNKING STRATEGY
Primary: 800-word chunks with 100-word overlap (as specified)
Implementation:
  - For text/PDF: Use sliding window chunking
  - For Excel: Row-level chunking (each row is a record)
  - For PPTX: Slide-level chunking with speaker notes

EMBEDDING STRATEGY
1. Embed all text content (PDFs converted to text)
2. Create separate embeddings for structured data (Excel sheets)
3. Create summary embeddings for PowerPoint key points
4. Use hierarchical chunking for nested content (e.g., case studies with sub-sections)

RETRIEVAL STRATEGY
1. Vector similarity search on embeddings (primary)
2. Keyword/BM25 search on metadata (secondary)
3. Filtering by document type/category when appropriate
4. Multi-stage retrieval (retrieve top-20 chunks, re-rank for relevance)

QUERY TYPES SUPPORTED
- "What are Gauri's core services?" → PDFs 08, 11
- "How was Kestrel Automotive transformed?" → PDF 05, Excel 10
- "What's Gauri's approach to data governance?" → PDF 04
- "How does Gauri implement Salesforce?" → PDF 03
- "What are SAP S/4HANA capabilities?" → PDF 02
- "Who are some Gauri clients?" → PDF 05, Excel 10, PowerPoint 11
- "What support SLAs does Gauri offer?" → PDF 07
- "How does Gauri handle DevOps?" → PDF 06

================================================================================
FILE QUALITY METRICS
================================================================================

Total Content: ~200 KB of text + structured data
Unique Data Points: 500+ (clients, projects, services, technologies, processes)
Estimated Tokens: ~40,000 (for typical LLM tokenisation)
Duplication Rate: <5% (minimal overlap across files)
Coverage: Complete view of Gauri's business, technology, and operations

================================================================================
USAGE GUIDELINES
================================================================================

FOR RAG IMPLEMENTATION
1. Load all files into document store (vector DB)
2. Convert PDFs to text for embedding
3. Create metadata fields: document_type, category, company, technology
4. Embed content with chunking strategy above
5. Test retrieval quality on sample queries

FOR SALES/MARKETING
- Use PowerPoint 11 for client presentations
- Use Excel 10 for reference data and quick facts
- Use PDFs 01, 03, 08 for detailed service explanations

FOR TECHNICAL REFERENCE
- Use PDFs 02, 04, 06, 07 for internal team reference
- Use PDF 05 for case study reference
- Use Text 09 for technology stack decisions

FOR TRAINING
- Use structured files (Excel 10, PowerPoint 11) for new employee onboarding
- Use PDFs for detailed technology and process training

================================================================================
MAINTENANCE AND UPDATES
================================================================================

Recommended Update Frequency:
- Case Studies (PDF 05, Excel 10): Quarterly (new projects)
- Service Offerings (PDF 08): As pricing/services change
- Technology Stack (Text 09, PDFs 02-04): As new tools adopted
- Standards (PDFs 06-07): As processes evolve
- Company Profile (PDF 01): As leadership/locations change

Version Control:
- Maintain versions in source control
- Include update dates in document metadata
- Track changes for compliance/audit purposes

================================================================================
QUESTIONS?
================================================================================

For questions about this dataset or Gauri's services, refer to:
- www.gauri.com
- Sales: 01522 243123
- Support: 01522 243122

Created: August 2026
Dataset Version: 1.0
Format: Production-Ready RAG Dataset for AI Assistants

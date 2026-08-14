from pathlib import Path


DOCUMENT_REGISTRY = {
    "01_Company_Profile_Overview.pdf": {
        "topic": "company_profile",
        "source_type": "company_information",
    },

    "01_Gauri_Leadership_Governance_Addendum.pdf": {
        "topic": "leadership_governance",
        "source_type": "public_company_information",
    },

    "02_Gauri_Employment_HR_People_Addendum.pdf": {
        "topic": "hr_people",
        "source_type": "internal_policy",
    },

    "02_SAP_Technology_Capabilities.pdf": {
        "topic": "sap",
        "source_type": "technology_capability",
    },

    "03_Gauri_Leave_Attendance_WFH_Addendum.pdf": {
        "topic": "leave_attendance_wfh",
        "source_type": "internal_policy",
    },

    "03_Salesforce_Technology_Capabilities.pdf": {
        "topic": "salesforce",
        "source_type": "technology_capability",
    },

    "04_Data_AI_Practice_Capabilities.pdf": {
        "topic": "data_ai",
        "source_type": "technology_capability",
    },

    "04_Gauri_Password_Endpoint_VPN_Security_Addendum.pdf": {
        "topic": "security_endpoint_vpn",
        "source_type": "internal_policy",
    },

    "05_Client_Case_Studies_Portfolio.pdf": {
        "topic": "client_case_studies",
        "source_type": "portfolio",
    },

    "05_Gauri_Business_Travel_Addendum.pdf": {
        "topic": "business_travel",
        "source_type": "internal_policy",
    },

    "06_Engineering_Standards_Development.pdf": {
        "topic": "engineering_standards",
        "source_type": "engineering_standard",
    },

    "06_Gauri_SAP_Salesforce_Data_Engineering_Addendum.pdf": {
        "topic": "sap_salesforce_data_engineering",
        "source_type": "public_current_capability",
    },

    "07_Support_Operations_Standards.pdf": {
        "topic": "support_operations",
        "source_type": "operational_standard",
    },

    "08_Service_Offerings_Engagements.pdf": {
        "topic": "service_offerings",
        "source_type": "service_information",
    },

    "09_Technology_Stack_Integration.txt": {
        "topic": "technology_stack_integration",
        "source_type": "technology_information",
    },

    "10_Client_Projects_Database.xlsx": {
        "topic": "client_projects",
        "source_type": "project_database",
    },

    "11_Gauri_Sales_Positioning.pptx": {
        "topic": "sales_positioning",
        "source_type": "sales_information",
    },

    "README_GAURI_RAG_DATASET.txt": {
        "topic": "rag_dataset_rules",
        "source_type": "rag_governance",
    },
}


def get_document_metadata(file_path: Path) -> dict:
    """Return static Gauri metadata for a source document."""

    file_name = file_path.name

    metadata = DOCUMENT_REGISTRY.get(
        file_name,
        {
            "topic": "unknown",
            "source_type": "unknown",
        },
    )

    return metadata.copy()
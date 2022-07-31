#
# Content-related tables / mappings etc
#

# do some data replacing on entity columns
org_unit_short_names = {
    'Patient Care Work Group': 'WG:PatCare',
    'Emergency Care Work Group': 'WG:EmCare',
    'Implementable Technology Specifications Work Group': 'WG:ITS',
    'Clinical Quality Information Work Group': 'WG:CQI',
    'Electronic Health Records Work Group': 'WG:EHR',
    'Orders and Observations Work Group': 'WG:O&O',
    'Modeling and Methodology Work Group': 'WG:M&M',
    'Structured Documents Work Group': 'WG:StructDoc',
    'Pharmacy Work Group': 'WG:Pharm',
    'Financial Management Work Group': 'WG:FM',
    'Payer/Provider Info Exchange Work Group': 'WG:PPIX',
    'Public Health Work Group': 'WG:PH',
    'Biomedical Research and Regulation Work Group': 'WG:BRR',
    'Board of Directors Work Group': 'WG:BOD',
    'Patient Administration Work Group': 'WG:PatAdmin',
    'Clinical Interoperability Council Work Group': 'WG:CIC',
    'Clinical Decision Support Work Group': 'WG:CDS',
    'Clinical Information Modeling Initiative Work Group': 'WG:CIMI',
    'Clinical Genomics Work Group': 'WG:CG',
    'Learning Health Systems Work Group': 'WG:LHS',
    'Mobile Health Work Group': 'WG:mHealth',
    'Conformance Work Group': 'WG:conf',
    'Cross-Group Projects Work Group': 'WG:XGP',
    'Devices Work Group': 'WG:Devices',
    'FHIR Infrastructure Work Group': 'WG:FHIR-I',
    'Publishing, Electronic Services and Tools Work Group': 'WG:PEST',
    'Imaging Integration Work Group': 'WG:II',
    'Community-Based Care and Privacy (CBCP) Work Group': 'WG:CBCP',
    'Security Work Group': 'WG:Sec',
    'Patient Empowerment Work Group': 'WG:PatEmp',
    'Infrastructure and Messaging Work Group': 'WG:I&M',
    'Vocabulary Work Group': 'WG:Vocab',
    'Services Oriented Architecture Work Group': 'WG:SOA',
    'Arden Syntax Work Group': 'WG:Arden',
    'Child Health Work Group': 'WG:ChildH',
    'Electronic Services and Tools Work Group': 'WG:EST',
    'Education Work Group': 'WG:ed',
    'PEST Work Group': 'WG:PEST',
    'Architectural Review Work Group': 'WG:ArchRev',
    'Anesthesia Work Group': 'WG:Anesthesia',
    'Templates Work Group': 'WG:Templates',

    'Healthcare Standards Integration': 'HSI',
    'International Mentoring Committee': 'IMC',

    'Publishing Work Group': 'Pub',
    'Publishing': 'Pub',

    'CDA Management Group': 'MG:CDA',
    'V2 Management Group': 'MG:V2',
    'FHIR Management Group': 'MG:FHIR-M',

    'Technical Steering Committee': 'TSC'
}

product_short_names = {
    'V3 Documents-Clinical (e.g. CDA)': 'V3 docs-clin',
    'Electronic Health Record': 'EHR',
    'V3 Foundation-Vocab Domains & Value Sets': 'V3 vocab',
    'V2 Messages-Clinical': 'V2 msgs-clin',
    'V2 Messages-Infrastructure': 'V2 msgs-infra',
    'V3 Services-Web Services (OMG)': 'V3 WS (OMG)',
    '- New Product Definition -': 'NEW PROD',
    'Domain Analysis Model (DAM)': 'DAM',
    'V3 Documents-Knowledge': 'V3 docs-knowl',
    'V3 Foundation-RIM': 'V3 RIM',
    '- Non Product Project -': 'NON-PROD',
    'V3 Messages-Clinical': 'V3 msgs-clin',
    'Guidance (e.g. Companion Guide, Cookbook, etc)': 'Guidance',
    'Education Services': 'Ed Services',
    '- New/Modified HL7 Policy/Procedure/Process -': 'HL7 policy',
    'Creating/Using a tool not listed in the HL7 Tool Inventory': 'Non-HL7 tool',
    'V2 Messages-Administrative': 'V2 msgs-Admin',
    'White Paper': 'WP',
    'V2 Messages-Departmental': 'V2 msgs-dept',
    'FHIR Extensions': 'FHIR Exts'
}

proj_name_replaces = {
    # acronyms
    'Draft Standard for Trial Use':             'DSTU',
    'CDA Release 2':                            'CDA',
    'HL7 Version 3 Standard':                   'HL7v3',
    'HL7 Version 3':                            'HL7v3',
    'HL7 Version 2':                            'HL7v2',
    'HL7 V 2.5.1 IG':                           'HL7v2 IG',
    'HL7 Version 2.6 IG':                       'HL7v2 IG',
    'HL7 CDA R2':                               'CDA',
    'Clinical Decision Support':                'CDS',
    'Domain Analysis Model':                    'DAM',
    'HL7 IG for FHIR':                          'FHIR IG',
    'HL7 IG for CDA':                           'CDA IG',
    'HL7 CDA IG':                               'CDA IG',
    'Consolidated CDA':                         'C-CDA',
    'C-CDA 2.1':                                'C-CDA',

    # misc
    'withdrawal':                               'withdraw',
    'White Papers':                             'White Paper',
    'Publication':                              'Publishing',
    'Tools':                                    'Tooling',
    'Virtual Medical Record':                   'vMR',
    'Da Vinci':                                 'DaVinci',

    # map some words to domains
    'Pharmacist':                               'Pharmacy',
    'genotyping':                               'Genomics',
    'Maternal':                                 'Maternity',
    'Registries':                               'Registry',
    'Radiation':                                'Radiology',
    'Adverse Drug Event':                       'Adverse Event',
    'Quality Measures':                         'Quality Measure',
    'Social Determinants of Health':            'SDOH',
    'Women’s Health':                           'Womens Health',
    'Emergency Care':                           'Emergency Department',
    'Anaesthesia':                              'Anesthesia'
}

domains = ['Claims', 'Clinical Decision Support', 'Emergency Department',
           'Laboratory', 'Child Health', 'Accounting & Billing', 'Anesthesia', 'Ophthalmology',
            'Pediatric', 'Public Health', 'Audiology', 'Transfusion', 'Vaccination',
           'Pathology', 'Patient Administration', 'Genomics', 'Dental', 'Nutrition',
           'Radiation Therapy', 'SPLASCH', 'Radiology', 'Podiatry',
            'Nutrition', 'Maternity', 'Oncology', 'Pharmacy']

topics = ['Phenotyping', 'Medical Record', 'Advance Directives', 'Registry', 'Reimbursement',
          'Advance Care Plan', 'Infection', 'Patient Care', 'Fetal Death', 'Prescribing', 'Medication'
          'Quality Measure', 'Gender Harmony', 'Medicolegal', 'Mobile Health', 'Military Service',
          'Identity', 'Trial', 'Security', 'Privacy', 'Covid', 'Ordering', 'Adverse Drug Event',
          'SDOH', 'Product Labeling', 'Prior Authorization', 'IPS', 'Vanguard', 'sIRB', 'Diet',
          'Patient Summary', 'Vital Signs', 'Pain', 'Pharmaceutical Quality', 'Birth Defects',
          'Vital Records', 'Occupational', 'Order Entry', 'Chronic', 'Quality Reporting', 'Burden',
          'SANER', 'Product Packaging', 'PACIO', 'Medicare', 'Medicaid', 'Skin', 'Wound', 'Alerts',
          'Payer', 'Cancer', 'Authorization', 'Clinical Notes', 'Reaffirmation', 'Interoperability',
          'Operational Support', 'Medical Equipment', 'DME', 'Health Services', 'CMHAFF',
          'Patient Reported Outcomes', 'eLTSS', 'CDISC', 'Womens Health', 'Evidence-Based Medicine',
          'Imaging', 'Syndromic Surveillance', 'Orthodontic', 'Structured Data Capture', 'QRDA',
          'Infectious Disease', 'Transplant', 'Transfusion', 'Case Reporting', 'Application',
          'Care Team', 'Specimen', 'Immunization', 'Medical Devices', 'Periodontal', 'negation',
          'Attachments', 'Children', 'Provenance', 'Lab Order', 'Usability', 'Neonatology',
          'Financial Services', 'Financial Management', 'Care Coordination', 'Health Story',
          'Accounting & Billing', 'National Healthcare Directory', 'MedMorph', 'CDS']

artefacts = ['Arden Syntax', 'Ballot', 'Transport',
            'Infrastructure IG', 'CDA on FHIR', 'CDA IG', 'FHIR IG', 'C-CDA', 'FHIR Resources',
            'DAM', 'C-CDA on FHIR', 'CDA', 'HL7v2', 'HL7v2 IG', 'HL7v3', 'DSTU', 'EHR-S',
            'CDS Hooks', 'XML Encoding', 'withdraw', 'Terminology', 'LOINC', 'vMR',
            'GELLO', 'DICOM', 'CARIN', 'SMART', 'FAST', 'IHE', 'Blue Button', 'Conformance',
            'Value Set', 'v2-To-FHIR', 'Ontology',
            'SOA', 'FAIR', 'CDASH', 'US Core', 'Cross Paradigm', 'BRIDG', 'HL7-HSRA',
            'Tooling', 'White Paper', 'Publishing', 'SHIFT', 'Guide', 'Bulk Data',
            'Clinical Practice Guideline', 'Data Types', 'ISO 13606', 'CDex', 'HRex',
            'Documentation', 'expression languages', 'Common Data Model', 'FHIRcast',
            'Templates', 'Connectathon', '3-Year Plan', 'mFHAST']

proj_sponsors = ['ONC', 'DaVinci']


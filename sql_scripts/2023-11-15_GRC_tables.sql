-- Database: GRC

-- DROP DATABASE IF EXISTS "GRC";

CREATE DATABASE "GRC"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_India.1252'
    LC_CTYPE = 'English_India.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;



CREATE TABLE activity_evidences (
    evidence_id serial4 NOT NULL,
    evidence_details text NULL,
    evidence_doc_path text NULL,
    CONSTRAINT activity_evidences_pkey PRIMARY KEY (evidence_id)
);



select * from grcs;

CREATE TABLE grcs (
    grc_id serial4 NOT NULL,
    grc_name varchar(255) NOT NULL,
    CONSTRAINT grcs_pkey PRIMARY KEY (grc_id)
);

CREATE TABLE master_documents (
    doc_id serial4 NOT NULL,
    doc_name varchar(255) NOT NULL,
    document_path text NULL,
    CONSTRAINT master_documents_pkey PRIMARY KEY (doc_id)
);

CREATE TABLE processes (
    process_id serial4 NOT NULL,
    process_name varchar(255) NOT NULL,
    description text NULL,
    CONSTRAINT processes_pkey PRIMARY KEY (process_id)
);
	
	
CREATE TABLE technologies (
    tech_id serial4 NOT NULL,
    tech_name varchar(255) NOT NULL,
    description text NULL,
    CONSTRAINT technologies_pkey PRIMARY KEY (tech_id)
);
	
CREATE TABLE users (
    user_id serial4 NOT NULL,
    user_name varchar(255) NOT NULL,
    phone_number varchar(20) NULL,
    email_id varchar(255) NOT NULL,
    create_date timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    update_date timestamp NULL,
    CONSTRAINT users_email_id_key UNIQUE (email_id),
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);	

CREATE TABLE notifications (
    notification_id serial4 NOT NULL,
    user_id int4 NULL,
    message text NOT NULL,
    CONSTRAINT notifications_pkey PRIMARY KEY (notification_id),
    CONSTRAINT notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE roles (
    role_id serial4 NOT NULL,
    role_name varchar(255) NOT NULL,
    grc_id int4 NULL,
    user_id int4 NULL,
    CONSTRAINT roles_pkey PRIMARY KEY (role_id),
    CONSTRAINT roles_grc_id_fkey FOREIGN KEY (grc_id) REFERENCES grcs(grc_id),
    CONSTRAINT roles_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE standards (
    standard_id serial4 NOT NULL,
    standard_name varchar(255) NOT NULL,
    grc_id int4 NULL,
    CONSTRAINT standards_pkey PRIMARY KEY (standard_id),
    CONSTRAINT standards_grc_id_fkey FOREIGN KEY (grc_id) REFERENCES grcs(grc_id)
);

CREATE TABLE domains (
    domain_id serial4 NOT NULL,
    domain_name varchar(255) NOT NULL,
    standard_id int4 NULL,
    CONSTRAINT domains_pkey PRIMARY KEY (domain_id),
    CONSTRAINT domains_standard_id_fkey FOREIGN KEY (standard_id) REFERENCES standards(standard_id)
);

CREATE TABLE practice (
    practice_id serial4 NOT NULL,
    practice_name varchar(255) NOT NULL,
    domain_id int4 NULL,
    CONSTRAINT practice_pkey PRIMARY KEY (practice_id),
    CONSTRAINT practice_domain_id_fkey FOREIGN KEY (domain_id) REFERENCES domains(domain_id)
);

CREATE TABLE standardrolemapping (
    mapping_id serial4 NOT NULL,
    standard_id int4 NULL,
    role_id int4 NULL,
    CONSTRAINT standardrolemapping_pkey PRIMARY KEY (mapping_id),
    CONSTRAINT standardrolemapping_role_id_fkey FOREIGN KEY (role_id) REFERENCES roles(role_id),
    CONSTRAINT standardrolemapping_standard_id_fkey FOREIGN KEY (standard_id) REFERENCES standards(standard_id)
);

CREATE TABLE subdomains (
    subdomain_id serial4 NOT NULL,
    domain_id int4 NULL,
    subdomain_name varchar(255) NOT NULL,
    objective text NULL,
    CONSTRAINT subdomains_pkey PRIMARY KEY (subdomain_id),
    CONSTRAINT subdomains_domain_id_fkey FOREIGN KEY (domain_id) REFERENCES domains(domain_id)
);

CREATE TABLE activities (
    activity_id serial4 NOT NULL,
    activity_name varchar(255) NOT NULL,
    doer_role_id int4 NULL,
    frequency varchar(50) NOT NULL,
    duration varchar(50) NOT NULL,
    doc_id int4 NULL,
    evidence_id int4 NULL,
    triggering_activity_id int4 NULL,
    approver_role_id int4 NULL,
    auditable bool NOT NULL,
    practice_id int4 NULL,
    CONSTRAINT activities_pkey PRIMARY KEY (activity_id),
    CONSTRAINT activities_approver_role_id_fkey FOREIGN KEY (approver_role_id) REFERENCES roles(role_id),
    CONSTRAINT activities_doc_id_fkey FOREIGN KEY (doc_id) REFERENCES master_documents(doc_id),
    CONSTRAINT activities_doer_role_id_fkey FOREIGN KEY (doer_role_id) REFERENCES roles(role_id),
    CONSTRAINT activities_evidence_id_fkey FOREIGN KEY (evidence_id) REFERENCES activity_evidences(evidence_id),
    CONSTRAINT activities_practice_id_fkey FOREIGN KEY (practice_id) REFERENCES practice(practice_id),
    CONSTRAINT activities_triggering_activity_id_fkey FOREIGN KEY (triggering_activity_id) REFERENCES activities(activity_id)
);

CREATE TABLE activity_assignment (
    assign_id serial4 NOT NULL,
    activity_id int4 NULL,
    user_id int4 NULL,
    start_date date NOT NULL,
    end_date date NULL,
    status varchar(255) NULL,
    audit_check bool NULL,
    approval_status varchar(255) NULL,
    approval_date date NULL,
    approver_user_id int4 NULL,
    create_date timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    update_date timestamp NULL,
    CONSTRAINT activity_assignment_pkey PRIMARY KEY (assign_id),
    CONSTRAINT activity_assignment_activity_id_fkey FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
    CONSTRAINT activity_assignment_approver_user_id_fkey FOREIGN KEY (approver_user_id) REFERENCES users(user_id),
    CONSTRAINT activity_assignment_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE controls (
    control_id serial4 NOT NULL,
    control_details text NOT NULL,
    subdomain_id int4 NULL,
    activity_id int4 NULL,
    CONSTRAINT controls_pkey PRIMARY KEY (control_id),
    CONSTRAINT controls_activity_id_fkey FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
    CONSTRAINT controls_subdomain_id_fkey FOREIGN KEY (subdomain_id) REFERENCES subdomains(subdomain_id)
);

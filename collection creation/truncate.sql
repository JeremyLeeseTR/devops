GRANT TRUNCATE ON w3rdtmcl."content" TO novusdocadmin;
GRANT TRUNCATE ON ALL TABLES IN SCHEMA wr3dtmcl TO novusdocadmin;

TRUNCATE TABLE w3rdtmcl."meta_content" CONTINUE IDENTITY RESTRICT;
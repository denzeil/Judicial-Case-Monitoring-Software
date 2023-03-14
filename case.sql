use Judiciary;

CREATE TABLE client_information (
    Case_ID varchar(50) NOT NULL,
    Client_name varchar(50) NOT NULL,
    Client_contact int NOT NULL,
    Case_type varchar(50) NOT NULL,
    Case_status varchar(50) NOT NULL,
    Appearances varchar(50) NOT NULL,
    Billing_ksh varchar(50) NOT NULL,
    Judge_ID varchar(50) NOT NULL,
    Hearing_date date NOT NULL,
    Next_hearing date NOT NULL,
    Laywer_name varchar(50) NOT NULL,
    Laywer_contact varchar(50) NOT NULL,
    PRIMARY KEY (Case_ID),
    FOREIGN KEY (Judge_ID) REFERENCES judge_information(Judge_ID),
    INDEX idx_judge_id (Judge_ID)
);
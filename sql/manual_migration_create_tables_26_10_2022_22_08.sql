CREATE TABLE tokens (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP 
);

CREATE TABLE tokens (
	token VARCHAR ( 50 ) NOT NULL,
	lemma VARCHAR ( 50 ),
	pos VARCHAR ( 50 ),
	tag VARCHAR ( 50 ),
	morph VARCHAR ( 50 ),
	ent_type VARCHAR ( 50 ),
	is_punct BOOLEAN ( 50 ),
	dep VARCHAR ( 50 ),
);
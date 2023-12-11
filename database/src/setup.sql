
CREATE TABLE MESSAGE (
    id_message INT PRIMARY KEY,
    date DATE NOT NULL,
    text TEXT NOT NULL
);

CREATE TABLE DOMAIN (
    name VARCHAR(255) PRIMARY KEY,
    used_counter INT  NOT NULL
);


CREATE TABLE GUESTBOOKMESSAGE (
    author VARCHAR(50) PRIMARY KEY,
    text TEXT NOT NULL,
    date DATE NOT NULL,
);



/* DATA EXAMPLES*/
INSERT INTO GUESTBOOKMESSAGE (author, text, date)
VALUES 
  ('John', 'Bonjour ! Merci de signer notre livre d\'or.', '2023-12-01'),
  ('Alice', 'C\'était une excellente expérience !', '2023-12-02'),
  ('Bob', 'Félicitations pour cet événement incroyable.', '2023-12-03');

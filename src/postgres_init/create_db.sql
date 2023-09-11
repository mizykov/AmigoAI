CREATE TABLE IF NOT EXISTS chat_history (
  message_id INT NOT NULL,
  role varchar(20) NOT NULL,
  text varchar(500) NOT NULL,
  PRIMARY KEY (message_id)
);

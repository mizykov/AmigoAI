CREATE TABLE IF NOT EXISTS chat_history (
  message_id INT NOT NULL,
  text varchar(50) NOT NULL,
  PRIMARY KEY (message_id)
);

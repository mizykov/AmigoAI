CREATE TABLE IF NOT EXISTS chat_history (
  message_id INT NOT NULL,
  role varchar(20) NOT NULL,
  text varchar(1000) NOT NULL,
  PRIMARY KEY (message_id)
);

CREATE TABLE IF NOT EXISTS scores_history (
  score_id INT NOT NULL,
  answer_id INT,
  score FLOAT,
  PRIMARY KEY (score_id)
);

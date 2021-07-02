
CREATE TABLE post (
  id          SERIAL          PRIMARY KEY,
  author      VARCHAR         NOT NULL,
  title       VARCHAR         NOT NULL,
  content     TEXT,
  time_       TIMESTAMP       NOT NULL
);

CREATE TABLE comment (
  id          SERIAL          PRIMARY KEY,
  post_id     INTEGER         NOT NULL  REFERENCES post(id),
  username    VARCHAR         NOT NULL,
  content     TEXT
  time_       TIMESTAMP       NOT NULL
);




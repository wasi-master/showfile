CREATE TABLE "topic"
  (
     "id"       INTEGER NOT NULL PRIMARY KEY,
     "forum_id" INTEGER NOT NULL,
     "subject"  VARCHAR(255) NOT NULL
  );

ALTER TABLE "topic"
  ADD CONSTRAINT forum_id FOREIGN KEY ("forum_id") REFERENCES "forum" ("id");

-- Initials
INSERT INTO "topic" ("forum_id", "subject")
  VALUES (2,  'D''artagnian');
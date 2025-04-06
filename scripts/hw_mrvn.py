#!../.venv/bin/python

import marvin

student = "Brave, daring, chivalrous, and sometimes a bit reckless."

def main(): 
  house = marvin.classify(
      student,
      labels=["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]
  )
  return house


if __name__ == "__main__":
    print(main())
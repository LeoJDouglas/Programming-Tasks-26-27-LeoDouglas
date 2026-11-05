"""
TASK: 04 Student Grades Table

# Use a dictionary of lists e.g
grades = {
  "Alice": [80, 85, 90],
  "Ben": [70, 60, 75]
}
Add:
- Function to compute class averages
- Function to add student
- Function to remove student

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
      grades = {    #dictionary is created
        "Alice": [80, 85, 90],
        "Ben": [70, 60, 75],
        "Charlie": [88, 92, 81],
        "Daisy": [76, 84, 79],
        "Ethan": [91, 87, 93],
        "Fiona": [65, 72, 68],
        "George": [83, 77, 89]
      }

      def average(grades):
        arr = list(grades.keys())
        total = 0
        totaltemp = 0
        for i in range(len(grades)):
            total += totaltemp
            temp = []
            temp.append(grades.get(arr[i]))
            for i in range(len(temp)):
                num = temp[i][0]
                totaltemp = int(num) + totaltemp
        average = total / len(arr)
        return average

      def add(grades):
          name = input("name ? ")
          grade = []
          for i in range(3):
              temp = input("Enter grade " + str(i + 1) +  " : ")
              grade.append(temp)
          grades[name] = grade
          return

      def remove(grades):
          key = input("who would you like to remove? ")
          grades.pop(key)
          return

      choice = input("Would you like the average, to add or to  remove? ")
      while choice != "":
          if choice == "average":
            print(average(grades))
          elif choice == "add":
              add(grades)
          elif choice == "remove":
              remove(grades)
          choice = input("Would you like the average, to add or to  remove? ")




      pass


if __name__ == "__main__":
    main()

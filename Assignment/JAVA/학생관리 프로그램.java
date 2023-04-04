// Student.java
public class Student {
    private String name;
    private String studentId;
    private String major;
    private int grade;

    public Student(String name, String studentId, String major, int grade) {
        this.name = name;
        this.studentId = studentId;
        this.major = major;
        this.grade = grade;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStudentId() {
        return studentId;
    }

    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public int getGrade() {
        return grade;
    }

    public void setGrade(int grade) {
        this.grade = grade;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", ID: " + studentId + ", Major: " + major + ", Grade: " + grade;
    }
}



//StudentManage.java

import java.util.Scanner;

public class StudentManager {
	
    private static final int MAX_STUDENTS = 100;
    private static Student[] students = new Student[MAX_STUDENTS];
    private static int studentCount  = 0;
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean running = true;
        while (running) {
            printMenu();
            try {
            	int choice = scanner.nextInt();
            	scanner.nextLine(); // Clear the buffer

            	switch (choice) {
                	case 1:
                		addStudent();
                		break;
                	case 2:
                		searchStudent();
                		break;
                	case 3:
                		modifyStudent();
                		break;
                	case 4:
                		deleteStudent();
                		break;
                	case 5:
                		displayAllStudents();
                		break;
                	case 6:
                		running = false;
                		break;
                	default:
                		System.out.println("Invalid choice. Please try again.");
            }
          }catch(NumberFormatException e) {
        	  System.out.println("Invalid input. Please enter a number.");
          }
       }     
    }

    private static void printMenu() {
        System.out.println("\nStudent Management System:");
        System.out.println("1. Add Student");
        System.out.println("2. Search Student");
        System.out.println("3. Modify Student");
        System.out.println("4. Delete Student");
        System.out.println("5. Display All Students");
        System.out.println("6. Exit");
        System.out.print("Enter your choice: ");
    }

    private static void addStudent() {
        System.out.print("Enter name: ");
        String name = scanner.nextLine();
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine();
        System.out.print("Enter major: ");
        String major = scanner.nextLine();
        System.out.print("Enter grade: ");
        int grade = scanner.nextInt();
        scanner.nextLine(); // Clear the buffer

        students[studentCount++] = new Student(name, studentId, major, grade);
        System.out.println("Student added successfully!");
    }

    private static void searchStudent() {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine();

        for (Student student : students) {
            if (student.getStudentId().equals(studentId)) {
              System.out.println(student.toString());
              return;
            } 
        }
        System.out.println("Student not found.");
	  }


	private static void modifyStudent() {
		System.out.print("Enter student ID: ");
		String studentId = scanner.nextLine();

		for (Student student : students) {
			if (student != null && student.getStudentId().equals(studentId)) {
          System.out.print("Enter new name (current name: " + student.getName() + "): ");
          String name = scanner.nextLine();
          System.out.print("Enter new major (current major: " + student.getMajor() + "): ");
          String major = scanner.nextLine();
          System.out.print("Enter new grade (current grade: " + student.getGrade() + "): ");
          int grade = scanner.nextInt();
          scanner.nextLine(); // Clear the buffer

          student.setName(name);
          student.setMajor(major);
          student.setGrade(grade);
          System.out.println("Student modified successfully!");
          return;
        }
    }
    System.out.println("Student not found.");
  }  

	private static void deleteStudent() {
		System.out.print("Enter student ID: ");
		String studentId = scanner.nextLine();

		for (int i = 0; i < studentCount; i++) {
			if (students[i].getStudentId().equals(studentId)) {
            for (int j = i; j < studentCount - 1; j++) {
                students[j] = students[j + 1];
            }
            studentCount--;
            System.out.println("Student deleted successfully!");
            return;
        }
    }
		System.out.println("Student not found.");
  }

	private static void displayAllStudents() {
		System.out.println("[Student List]");
		for (int i = 0; i < studentCount; i++) {
			System.out.println((i + 1) + ". " + students[i].toString());
		}
	}
}



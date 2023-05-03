// Student.java

public class Student {
    private String name;
    private String studentId;
    private String major;
    private double grade;

    public Student(String name, String studentId, String major, double grade) {
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

    public double getGrade() {
        return grade;
    }

    public void setGrade(double grade) {
        this.grade = grade;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", ID: " + studentId + ", Major: " + major + ", Grade: " + grade;
    }
}

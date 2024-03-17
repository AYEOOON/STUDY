// #include <stdio.h>
// #include <string.h>

// struct Student
// {
//   int no;
//   char name[20];
//   double g;
//   char tel[20];
// };

// void swap(int* a, int* b)
// {
//   int temp = *a;
//   *a = *b;
//   *b = temp;
// }

// void main()
// {
//   // int num;
//   // double num1;
//   //struct Student stu;
//   //struct Student stu[10];
//   struct Student stu1, stu2;

//   stu1.no = 1;
//   stu2.no = 2;

//   stu1.g = 3.0;
//   stu2.g = 4.0;

// // 구조체 안에 있는 Swap함수를 만드는데 안에 있는 학점만 바꿔라.. 이런 느낌의 문제를 낼수도 있다. 
//   printf("변경 후\n");
//   swap(&stu1.no, &stu2.no);

//   printf("%d\n", stu1.no);
//   printf("%d", stu2.no);

//   // stu.no = 123;
//   // //stu.name = '홍길동'; // 이렇게하면 오류발생
//   // strcpy(stu.name, "홍길동");

//   // printf("%d : %s", stu.no, stu.name);

//   // printf("학점입력 : ");
//   // scanf("%lf", &stu.g);
//   // printf("전화번호입력 : ");
//   // scanf("%lf", stu.tel); // 문자열로 입력받을 때는 &을 쓰지 않음

//   // printf("%f : %s" , stu.g, stu.tel);

//   // struct Student *p;

//   // p = (struct Student*)malloc(sizeof(struct Student));

//   // p->no = 123;

//   // printf("no: %d\n", p->no);
//   // printf("학점 입력: ");
//   // scanf("%lf", &p->g);
//   // printf("학점 : %f\n", p->g );
//   // printf("이름 입력 : ");
//   // scanf("%s", p-> name);
//   // printf("이름: %s\n", p->name);

//   // stu[0].no = 123;
//   // scanf("lf", &stu[0].g);


  
// }

#include <stdio.h>
#include <string.h>

typedef struct Book
{
  int no;
  char B_name[20];
  int a;
  int b;
}Book;

void Ser(Book book[], int sel, int val, int count)
{
  switch(sel){
    case 1:
      for(int k = 0; k <= count; k++){
        if (book[k].no == val){
          printf("%10d%10s%10d%10d/n", book[k].no, book[k].B_name, book[k].a, book[k].b);
        }
      }
    return;

    case 2:
      for(int k = 0; k <= count; k++){
        if (book[k].a == val){
          printf("%10d%10s%10d%10d/n", book[k].no, book[k].B_name, book[k].a, book[k].b);
        }
      }
    return;
    
    case 3:
      for(int k = 0; k <= count; k++){
        if (book[k].no == val){
          printf("%10d%10s%10d%10d/n", book[k].no, book[k].B_name, book[k].a, book[k].b);
        }
      }
    return;
    
  default:
    break;
  }
  
};


void main(){
  Book book[20];
  int count = 3, sel = 1;

  book[0].no = 1111;
  strcpy(book[0].B_name, "자료구조");
  book[0].a = 315;
  book[0].b = 320;

  book[1].no = 1111;
  strcpy(book[1].B_name, "자바");
  book[0].a = 310;
  book[0].b = 320;

  book[2].no = 2222;
  strcpy(book[2].B_name, "자바");
  book[2].a = 302;
  book[2].b = 308;

  book[3].no = 3333;
  strcpy(book[2].B_name, "자바");
  book[3].a = 320;
  book[3].b = 325;

  while(sel)
    {
      printf("1. 신규대여\n2. 조회\n3. 선택: ");
      scanf("%d", &sel);

      switch(sel){
        case 1:
          count++;
          printf("학번 :");
          scanf("%d", &book[count].no);
          printf("책제목 :");
          scanf("%s", book[count].B_name);
          printf("대여일 :");
          scanf("%d", &book[count].a);
          printf("반납일 :");
          scanf("%d", &book[count].b);
          break;


        case 2:
          printf("--검색방법--\n1. 학번\n2. 대여일\n3. 반납일\n선택: ");
          scanf("%d", &sel);
          printf("검색할 겂: ");
          int val;
          scanf("%d", &val);

          Ser(book, sel, val, count);
      }
    }
}

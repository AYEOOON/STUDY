#include <stdio.h>
#include <stdlib.h>// 동적할당에 관한 라이브러리 포함

// void main()
// {
//   // // int* p;
//   // // while (1){
//   // //   p = malloc(40);   // 메모리 누수, 메모리를 과도하게 잡아먹음
//   // // }
//   // int a;
  
//   // int *p = malloc(4); // 4바이트만큼 확보
//   // // *p = 1;
//   // // void* 어떠한 것이든 포인터로 변경 가능하다.
//   // // void 어떤것도 리턴하지 않는다.

//   // printf("%p\n", *p);
//   // //*(p+1) = 2;
//   // // printf("%p\n", *(p+1)); // 정상출력됨, 다른 응용프로그램에서 확보된 공간은 침범하지 못함, 따라서 그냥 메모리 공간을 마음대로 쓸수 있음, 값이 강제로 바뀐것


//   // int a[10];

//   // int *cp = calloc(10, 4); //40 바이트 할당
//   // //int *cp = calloc(40, 1); //정상 출력, 공간 확보는 동일하기 때문
//   // int *cp = calloc(1, 40); // 정상출력, 동일
//   // //int *mp = malloc(40); // 이것과 같다. 하지만 초기화는 하지않는다는 차이점이 있다. 

//   int a;

//   int *cp = calloc(1, 4);
  
//   *cp = 10;
//   printf("%d\n", *cp);

//   //cp = realloc(cp, 80); // 이런식으로 늘리거나 빼거나 가능

//   free(cp); // 동적할당 해지
//   printf("%d\n", *cp);
//   *cp = 30; // 주소는 남아있음, 거기에 동적할당만 해지했기 때문, 하지만 다른 프로그램도 사용가능하기 때문에 접근다능하다. 
//   printf("%d\n", *cp);

// }

typedef struct Student{
  int no;
  char name[20];
  int m; 
  int f;
}Stu;

void Insert(Stu* stu_p, int start, int end){
  printf("------입력-------\n");
  for(int k = start; k< end; k++){
    printf("---%d번 학생---\n", k+1);
    printf("학번 : ");
    //scanf("%d", &(stu_p+k)->no); // 시험 문제로 여길 비워놓으면..
    scanf("%d", &stu_p[k].no);
    printf("이름 : ");
    //scanf("%d", &(stu_p+k)->no); // 시험 문제로 여길 비워놓으면..
    scanf("%s", stu_p[k].name);
    printf("중간 : ");
    //scanf("%d", &(stu_p+k)->no); // 시험 문제로 여길 비워놓으면..
    scanf("%d", &stu_p[k].m);
    printf("기말 : ");
    //scanf("%d", &(stu_p+k)->no); // 시험 문제로 여길 비워놓으면..
    scanf("%d", &stu_p[k].f);
  }
};

void Sort(Stu* stu_p,int n){
  for(int k = n-1; k > 0; k --){
    for(int w = 0; w < k; w++){
      if (stu_p[w].m + stu_p[w].f < stu_p[w+1].m + stu_p[w+1].f){
        Stu tmp = stu_p[w];
        stu_p[w] = stu_p[w+1];
        stu_p[w+1] = tmp;
      }
    }
  }
};


void Display(Stu* stu_p,int n){
  printf("\n성적순위\n");
  for (int k = 0; k < n; k++){
    printf("%d등 : %d\n", k + 1, stu_p[k].no);
  }
  printf("------끝------");
};


void main(){
  int n;
  int m;
  printf("인원 수 입력 : ");
  scanf("%d", &n);
  Stu *stu_p = malloc(n*sizeof(Stu));
  //int *stu_p = calloc(n, n*sizeof(Stu));

  Insert(stu_p, 0, n);
  Sort(stu_p, n);
  Display(stu_p, n);

  printf("\n추가할 인원 수 입력 : ");
  scanf("%d", &m);
  stu_p = realloc(stu_p, n*sizeof(Stu)+m);
  Insert(stu_p, n, m+n);
  Sort(stu_p, n+m);
  Display(stu_p, n+m);
}

#include <stdio.h>
int main()
{int a,e,b,c,f;
    printf("\t\tCALCULATOR\n");
printf("What u want to do:");
printf("\nAddition:(press 1):\n");
printf("Subtraction:(press 2):\n");
printf("Multiplication:(press 3):\n");
printf("Division:(press 4):\n");
printf("Exit:(press 5):\n");
scanf("%d",&f);
switch(f)
{ case 1: {printf("Enter the numbers u want to add:\n");printf("Enter 1st number:");
    scanf("%d",&e);printf("Enter 2nd number:");
    scanf("%d",&b);
    c=e+b;
    printf("%d",c);}break;
    case 2:
        {
            printf("Enter the numbers u want to subtract:");printf("\nEnter 1st number:");
            scanf("%d",&e);printf("Enter 2nd number:");
            scanf("%d",&b);
            c=e-b;
            printf("%d",c);
        }break;
    case 3:
        {
            printf("Enter the numbers u want to multiply:");
            printf("\nEnter the 1st number:");
            scanf("%d",&a);
            printf("Enter 2nd number:");
            scanf("%d",&b);
            c=a*b;
            printf("%d",c);
        }break;
         case 4:
        {
            printf("Enter the numbers u want to divide:");
            printf("\nEnter the 1st number:");
            scanf("%d",&a);
            printf("Enter 2nd number:\n[It must be non zero]:");
            scanf("%d",&b);
            float c;
            c=(float)a/b;
            printf("%.2f",c);
        }break;
        case 5:
   printf("Thanks!!!");
   break;
        default:
            printf("Invalid value");break;
}
    return 0;
}

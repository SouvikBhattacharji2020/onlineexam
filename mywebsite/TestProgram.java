/*
WAP to find out 3 digit number whether it is prime or not and if it is not prime within the divisible number then check.
how many even number is present within it
*/

import java.util.*;
public class MyClass {
    public static void main(String args[]) 
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter a number :-");
     int a=sc.nextInt();
     int m=0,n=0;
     if(a>99 && a<=999)
     {
      for(int i=1;i<=a;i++)
      {
          if(a%i==0)
          {
              if(i%2==0)
              {
                n++;    
               System.out.print(i+" , ");
              
              }
             m++;
            // System.out.print(i+"  ");
          }
      }
      System.out.println();
         if(m==2){
             System.out.println("This is a Prime Number.");
            }
        else{
           System.out.println("This is a Not Prime Number.");
           System.out.println("The number of even multiple is :"+n);
        }
       
     }
     else{
          System.out.println("Not within the given range.");
      }  
    }
}
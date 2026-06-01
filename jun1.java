public class jun1 {
    public static void main(String[] args) {
        System.out.println("Hello World in java using visual studio code");
        // EASY -> 1st
        System.out.println("Prabha");
        // 2nd
        System.out.println("College Name : Malla Reddy University");
        // 3rd
        int a = 10;
        int b = 20; 
        int sum = a+b;
        System.out.println("sum= "+ sum);
        // 4th 
        int length = 8;
        int breadth = 10;
        int rectArea  = length * breadth;
        System.out.println("Area of rectangle : "+ rectArea);
        // 5th 
        double radius = 7.9;
        double circleArea = Math.PI * radius * radius;
        System.out.println("Area of circle= "+circleArea);

        // MEDIUM -> 6th 
        int x = 100;
        int y = 200;
        int temp = x;
        x = y;
        y = temp;
        System.out.println("After Swap:x= "+ x+ ",y = " +y);
        // 7th 
        double celsius = 37.0; 
        double fahrennheit = (celsius * 9/5) +32;
        System.out.println("Fahrenheit= " + fahrennheit);
        // 8th 
        int p = 45;
        int q = 49;
        if (p > q) 
            System.out.println("LArgest of two = "+p);
        else 
            System.out.println("Largest of two = "+q);
        // 9th 
        int n1 = 15; 
        int n2 = 20;
        int n3 = 30;
        if(n1 >=n2 && n1>=n3)
            System.out.println("Largest of three ="+n1);
        else if(n2 >=n1 && n2>=n3)
            System.out.println("Largest of three ="+n2);
        else 
             System.out.println("Largest of three ="+n3);
        // 10th 
        int n = 19;
        if (n %2 == 0 )
            System.out.println(n + " is even ");
        else 
            System.out.print(n + " is odd");


    }
}


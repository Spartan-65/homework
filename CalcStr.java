package test;

import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
import java.util.concurrent.LinkedBlockingQueue; 
  
public class CalcStr {  
  
    static String operator = "+-*/%^()s";    
    public static String pretreatment(String str) {
    	str=str.replace("?", "/");
    	str=str.replaceAll("?", "*");
    	str=str.replace("e", Math.E+"");
    	str=str.replace("?",Math.PI+"");
        StringBuffer sb = new StringBuffer(str);  
        for (int i = 0; i < sb.length(); i++) {  
            char c = sb.charAt(i);  
            if (operator.indexOf(c) >= 0) {  
                if (i == 0) {  
                    sb.insert(0, '0');  
                    i++;  
                } else if (sb.charAt(i - 1) == '(') {  
                    sb.insert(i, '0');  
                    i++;  
                }  
            }
        }
        
        str=sb.toString();
        str=str.replace("sin(", "s");
        str=str.replace("?(", "l");
        str=str.replace("v(", "r");
        str=str.replace("lg(", "L");
        System.out.println(str);
        return str;
    }   
    public static int opcompare(char op1, char op2) {  
        if (op1 == '('||op1=='s') {   
            return 1;  
        }  
        if ('^' == op1) {  
            if (op2 == '^') {  
                return 0;  
            }  
            return -1;  
        } else if ("+-".indexOf(op1) >= 0) {  
            if ("+-".indexOf(op2) >= 0) {  
                return 0;  
            }  
            return 1;  
        } else  
        {  
            if ("+-".indexOf(op2) >= 0) {  
                return -1;  
            } else if ('^' == op2) {  
                return 1;  
            }  
            return 0;  
        }  
    }
    
    
    
    public static double Calculator(String s) throws Exception {   
        String prestr = pretreatment(s);    
        LinkedBlockingQueue<String> polish = new LinkedBlockingQueue<String>();   
        StringBuffer temp = new StringBuffer();  
          
        Stack<Character> stack = new Stack<Character>();  
        for (int i = 0; i < prestr.length(); i++) {  
  
            char c = prestr.charAt(i);   
            if (operator.indexOf(c) >= 0) {  
                if (temp.length() > 0) { 
                    polish.offer(temp.toString());  
                    temp = new StringBuffer();  
                }  
                switch (c) {  
                case '(':  
                    stack.push(c);  
                    break;
                case 's':
                	stack.push(c);
                	break;
                case ')':  
                    while (stack.size() > 0) {  
                        char op = stack.pop();  
                        if (op != '(') {  
                            polish.offer(String.valueOf(op));
                            if(op=='s')break;
                        } else {  
                            break;  
                        }  
                    }  
                    break;  
                default:  
                    if (stack.size() == 0) {  
                        stack.push(c);  
                    } else {  
                        while (stack.size() > 0) {  
                            char op1 = stack.lastElement(); 
                            int com = opcompare(op1, c);  
                            if (com <= 0) {  
                                polish.offer(String.valueOf(stack.pop()));  
                            } else {  
                                stack.push(c);  
                                break;  
                            }  
                        }  
                        if (stack.size() == 0) {  
                            stack.push(c);  
                        }  
                    }  
                    break;  
                }  
            } else {  
                temp.append(c);  
            }  
        }  
        if (temp.length() > 0) {  
            polish.offer(temp.toString());  
        }  
        while (stack.size() > 0) {  
            polish.offer(String.valueOf(stack.pop()));  
        }  
        System.out.println("Calcstra Queue:" + polish.toString());  
  
        return CalcstraWithQueue(polish);  
    }
    
    
    
    public static double CalcstraWithQueue(Queue<String> que) throws Exception {  
        Stack<Double> stack = new Stack<Double>();  
        while(true)  
        {  
        	String str = que.poll();  
        if(str == null)
        {  
            break;  
        }  
        if (operator.indexOf(str) >= 0) {  
              
            double num2 = stack.pop();  
            double num1 = stack.pop();  
            double tempresult = 0;  
            switch (str.charAt(0)) {  
            case '+':  
                tempresult = num1 + num2;  
                break;  
            case '-':  
                tempresult = num1 - num2;  
                break;  
            case '*':  
                tempresult = num1 * num2;  
                break;  
            case '/':  
                if(num2 == 0)  
                {  
                    throw new Exception("Error: divisor is 0");  
                }  
                tempresult = num1 / num2;  
                break;  
            case '%':  
                tempresult = num1 % num2;  
                break;  
            case '^':  
                tempresult = Math.pow(num1, num2);  
                break;
            case 's':
            	tempresult=Math.sin(num2);
            	stack.push(num1);
            	break;
            default:  
                throw new Exception("Operator:" + str + "unrecognized!");  
            }  
            stack.push(tempresult);  
        } else {  
            stack.push(Double.valueOf(str));  
        }  
        }  
        return stack.pop();  
    }
    
    
    
    public static double getresult(String s) {  
        double result = 0;  
        try {
            result = Calculator(s);  
        } catch (Exception e) {   
            e.printStackTrace();  
        }  
	    return result;
    }
}  
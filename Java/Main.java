import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.io.*;

public class Main
{
	public static void main(String[] args) {
	    String result="";
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String input=br.readLine();
		while(input.length()>0)
		{
			char[] charArray = input.toCharArray();
			Map map = new HashMap();
			for (Character character : charArray) {
			if (map.containsKey(character)) {
			map.put(character, map.get(character) + 1);
			} else {
			map.put(character, 1);
			}
			}

		}
	}
}
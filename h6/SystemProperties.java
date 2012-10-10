import java.util.Arrays;
import java.util.Collections;

public class SystemProperties {
	public static void printArgs(String[] args) {
		for(int i = 0; i < args.length; i++) {
			if(System.getProperty(args[i]) != null) {
				System.out.println(System.getProperty(args[i]));
			}
		}
	}

	public static void main(String[] args) {
		if(args[args.length - 1].equals("down")) {
			Arrays.sort(args, Collections.reverseOrder());
		}else {
			Arrays.sort(args);
		}
		printArgs(args);
	}	
}
import java.util.*;
public class UEQuantifier {
	public static boolean universal(Set<Integer> set) {
		for (int element : set) {
			if (element < 5 || element > 200)
				return false;
		}
		return true;
	}
	public static boolean existential(Set<Integer> set) {
		for (int element : set) {
			if (element >= 50){
				return true;
			}
		}
		return false;
	}
	public static int setFunc(int setVar) {
		int next_element = 2*setVar + 3;
		return next_element;
	}
	public static Set<Integer> buildSet() {
		Set<Integer> set = new HashSet<>();
		for (int i = 1; i<=100; i++) {
			set.add(setFunc(i));
		}
		return set;
	}
	public static void main(String[] args) {
		Set<Integer> my_set = buildSet();
		System.out.println(my_set);
		if (universal(my_set)) {
			System.out.println("The universal quantifier statement is true");
		}
		else {
			System.out.println("The universal quantifier statement is false");
		}
		if (existential(my_set)){
			System.out.println("The existential quantifier statement is true");
		}
		else {
			System.out.println("The existential quantifier statement is false");
			

		}
	}
}


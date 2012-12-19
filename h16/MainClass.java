package org.elsys.eval;

public class MainClass {

	/** 
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DirectEvaluatorFactory fact = new DirectEvaluatorFactory();
		AbsoluteEvaluatorFactory absFactory = new AbsoluteEvaluatorFactory();
		IEvaluator sum = fact.createFibonaciEvaluator();
		
		IEvaluator abs = absFactory.createFibonaciEvaluator();
		abs.add(-100);
		abs.add(20);
		System.out.println(abs.evaluate());
		sum.add(3);
		sum.add(1);
		
		System.out.println(sum.evaluate());
	}

}

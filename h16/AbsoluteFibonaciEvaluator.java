package org.elsys.eval;

public class AbsoluteFibonaciEvaluator extends FibonaciEvaluator implements IEvaluator {

	public AbsoluteFibonaciEvaluator() {
		super();
	}
	
	@Override
	public void add(double d) {
		super.add(Math.abs(d));
	}

	@Override
	public Double evaluate() {
		return super.evaluate();
	}

}

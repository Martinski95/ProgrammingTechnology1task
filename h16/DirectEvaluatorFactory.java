package org.elsys.eval;

public class DirectEvaluatorFactory implements IEvaluatorFactory {

	@Override
	public IEvaluator createSumEvaluator() {
		SumEvaluator sum = new SumEvaluator();
		return sum;
	}

	@Override
	public IEvaluator createPowerOnEvaluator() {
		PowerOnEvaluator pow = new PowerOnEvaluator();
		return pow;
	}

	@Override
	public IEvaluator createPowerOnEvaluator(double power) {
		PowerOnEvaluator pow2 = new PowerOnEvaluator(power);
		return pow2;
	}

	@Override
	public IEvaluator createFibonaciEvaluator() {
		FibonaciEvaluator fib = new FibonaciEvaluator();
		return fib;
	}

}

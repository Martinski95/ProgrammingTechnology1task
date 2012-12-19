package org.elsys.eval;

public class AbsoluteEvaluatorFactory implements IEvaluatorFactory {

	@Override
	public IEvaluator createSumEvaluator() {
		AbsoluteSumEvaluator absSum = new AbsoluteSumEvaluator();
		return absSum;
	}

	@Override
	public IEvaluator createPowerOnEvaluator() {
		AbsolutePowerOnEvaluator absPow = new AbsolutePowerOnEvaluator();
		return absPow;
	}

	@Override
	public IEvaluator createPowerOnEvaluator(double power) {
		AbsolutePowerOnEvaluator absPow2 = new AbsolutePowerOnEvaluator(power);
		return absPow2;
	}

	@Override
	public IEvaluator createFibonaciEvaluator() {
		AbsoluteFibonaciEvaluator absFib = new AbsoluteFibonaciEvaluator();
		return absFib;
	}

}

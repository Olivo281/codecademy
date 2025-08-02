    Probability (pp): This is the likelihood of an event happening. It ranges from 0 to 1.

    Example: If a soccer team has a 70% chance of winning, then p=0.7p=0.7.

    Odds (p1−p1−pp​): This is the ratio of the probability of success to the probability of failure.
    Odds=p1−p
    Odds=1−pp​

    Example: If p=0.7p=0.7, then:
    Odds=0.71−0.7=0.70.3=2.33
    Odds=1−0.70.7​=0.30.7​=2.33

    This means the event is 2.33 times more likely to happen than not.

    Logit function: The logit function takes probability and converts it into log-odds (logarithm of the odds):
    logit(p)=log⁡(p1−p)
    logit(p)=log(1−pp​)

    For p=0.7p=0.7:
    \logit(0.7)=log⁡(2.33)≈0.847
    \logit(0.7)=log(2.33)≈0.847

    This log-odds value can take any value from −∞−∞ to +∞+∞, making it useful for logistic regression.

Inverse: Getting Probability from Log-Odds

If we have log-odds xx, we can convert it back to probability using the sigmoid function:
p=11+e−x
p=1+e−x1​

For x=0.847x=0.847:
p=11+e−0.847≈0.7
p=1+e−0.8471​≈0.7
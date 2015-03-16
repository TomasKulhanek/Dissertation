class Cardiovascular.Examples.DizertaceExample.twoball
  parameter Real hydraulicconductor1.G = 1.0;
  Real hydraulicconductor1.qin.q;
  Real hydraulicconductor1.qin.p;
  Real hydraulicconductor1.qout.q;
  Real hydraulicconductor1.qout.p;
  Real hydraulicelastance1.V(start = 5000.0);
  parameter Real hydraulicelastance1.V0 = 529.0;
  parameter Real hydraulicelastance1.p0;
  parameter Real hydraulicelastance1.C = 1.5;
  Real hydraulicelastance1.qin.q;
  Real hydraulicelastance1.qin.p;
  Real hydraulicelastance2.V;
  parameter Real hydraulicelastance2.V0 = 2845.0;
  parameter Real hydraulicelastance2.p0;
  parameter Real hydraulicelastance2.C = 200.0;
  Real hydraulicelastance2.qin.q;
  Real hydraulicelastance2.qin.p;
equation
  hydraulicconductor1.qin.q = -hydraulicconductor1.qout.q;
  -hydraulicconductor1.qin.q = hydraulicconductor1.G * (hydraulicconductor1.qout.p - hydraulicconductor1.qin.p);
  hydraulicelastance1.qin.p - hydraulicelastance1.p0 = if hydraulicelastance1.V < hydraulicelastance1.V0 then 0.0 else (hydraulicelastance1.V - hydraulicelastance1.V0) / hydraulicelastance1.C;
  hydraulicelastance1.qin.q = der(hydraulicelastance1.V);
  hydraulicelastance2.qin.p - hydraulicelastance2.p0 = if hydraulicelastance2.V < hydraulicelastance2.V0 then 0.0 else (hydraulicelastance2.V - hydraulicelastance2.V0) / hydraulicelastance2.C;
  hydraulicelastance2.qin.q = der(hydraulicelastance2.V);
  hydraulicconductor1.qin.q + hydraulicelastance1.qin.q = 0.0;
  hydraulicconductor1.qout.q + hydraulicelastance2.qin.q = 0.0;
  hydraulicconductor1.qout.p = hydraulicelastance2.qin.p;
  hydraulicconductor1.qin.p = hydraulicelastance1.qin.p;
end Cardiovascular.Examples.DizertaceExample.twoball;


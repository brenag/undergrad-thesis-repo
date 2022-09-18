T=readtable('experiment.csv');
     %       ^^^^^^^^^------ your csv filename

sdot_meas = T{:,:};
save('s_dot.mat','sdot_meas');
  %   ^^^^^^^^^----- your resulting .mat filename   

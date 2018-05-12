#!/usr/bin/python
# probe,database seting 
import string
import re
f=open('./inputprobe.tcl','w+')
f.writelines(['# This is the NC-SIM(R) probe command file used in AMS-ADE integration\n'])
f.writelines(['if { [info exists ::env(AMS_RESULTS_DIR) ] } { set AMS_RESULTS_DIR $env(AMS_RESULTS_DIR)} else {set AMS_RESULTS_DIR "../psf"}\n'])
f.writelines(['database -open ams_database -shm -into ${AMS_RESULTS_DIR} -default\n'])
f.writelines(['database -open waves -into resultDirName.shm -default \n'])
f.writelines(['probe -create -database waves -all -depth -all\n'])

#probe control/clk signal
#seq=['tb_phase_ch','tb_switch_en_train','tb_switch_en_test','tb_switch_en','tb_arb_clk','tb_jk_clk','tb_jk_train_clk','tb_jk_test_clk','tb_lu_src_clk','tb_lu_clk','tb_sampling_y','tb_amp_n','tb_amp_n_sx','tb_amp_n_sy','tb_amp_out','tb_amp_out_sx','tb_amp_out_sy','tb_s_weight_xbias','tb_s_weight_ybias']
seq=['tb_jk_clk','tb_switch_en']
for i in seq:
   f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.',i,'}\n'])
# probe x,y input output voltage


xnum=24
ynum=24

# x layer neuron signal
for i in range(1,xnum+1):
  i= '%d'%i  
  #x layer neuron module signal probe
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_xTrain_src[',i,']}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_x_in[',i,']}\n'])
  
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_x_sum[',i,']}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].xcell.I_c_1.P1N0}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].xcell.I_c_1.P0N1}\n'])


  f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_x_out_res[',i,']}\n'])

  #x layer switch module signal probe
  #f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.X[',i,'].s_x.IO}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_s_x_io[',i,']}\n'])
 
  #f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.X[',i,'].s_x.I_ccvs.PS}\n'])  
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].s_x.I_ccvs.PS}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].s_x.I_ccvs.P}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].s_x.io_mode}\n'])
  
  #x layer arb module signal probe
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_arb_x_sum[',i,']}\n'])
  f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_en_lu_x[',i,']}\n'])
  
  #x layer weight current bias probe
  #f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.X[',i,'].Res_X.p}\n'])



# y layer neuron signal
for j in range(1,ynum+1):
  j= '%d'%j 
  #y layer neuron module signal probe
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_yTrain_src[',j,']}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_yTest_src[',j,']}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_yTest_out[',j,']}\n'])


  f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_y_in[',j,']}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_y_sum[',j,']}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.Y[',j,'].ycell.I_c_1.P1N0}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.Y[',j,'].ycell.I_c_1.P0N1}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_y_out[',j,']}\n'])

  #y layer switch module signal probe
  #f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.Y[',j,'].s_y.IO}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_s_y_io[',j,']}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].s_x.I_ccvs.PS}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.X[',i,'].s_x.I_ccvs.PS}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.X[',i,'].s_x.I_ccvs.P}\n'])

  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.Y[',j,'].s_y.io_mode}\n'])
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_arb_y_sum[',j,']}\n'])

  #y layer arb module signal probe
  #f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_arb_y_sum[',j,']}\n'])
  f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.tb_en_lu_y[',j,']}\n'])
  
  # y layer weight bias probe
  #f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.Y[',j,'].Res_Y.p}\n'])
 
'''
# probe synapse voltage/current
for i in range(1,xnum+1):
   i= '%d'%i  
   for j in range(1,ynum+1):
         j= '%d'%j 
	 f.writelines(['probe -create -emptyok -database ams_database {Top_Recall_Only.Row[',i,'].r.Column[',j,'].I_mr_weight.P}\n'])
         f.writelines(['probe -create -emptyok -database ams_database -flow {Top_Recall_Only.Row[',i,'].r.Column[',j,'].I_mr_weight.P}\n'])
'''




# memristor based BAM Neural Network Implemented by Verilog-AMS 

## Overview
-----------------------------------------------
<!--project purpose--> 
This project is aim at the system level
design of memristor-based BAM neural network circuits when both digital and analog circuits are employed. 
<!--;brief illustration of Verilog-AMS-->
Verilog-AMS is a hardware description language which is an extension of Verilog capable of design digital, analog and mix-signal circuits 
<!--;brief illustration of Cadence virtuoso,spectre and AMS designer -->
The feature of Verilog-AMS laguage can be supported by the Candece ltd.co product Virtuoso platform with related sub-product module installed on this platform, namely, the Spetre simulator for analog IC, Incisive for digital circuit, the mixed mode simulator product MMSIM 
For illustration purpose, if we make an analogy, virtuoso is to Powerpoint and ams is to MathType 


## Dependency
-----------------------------------------------
* Cadence Virtuoso <font face= "times new man" size =5>Platform must be installed, the version is asked for IC617 or higher</font>,
* INCISIVE <font face= "times new man" size =5> coupled with the AMS designer installed. the detailed product ID for run Verilog-AMS is INCISIVE151 MMSIM151
* MMSIM <font face= "times new man" size =5> 

## Sample Code Illustration of Verilog-AMS Design
-----------------------------------------------
### Voltage Source 


### passive Device instantiation 

### test pattern generation
For more details about Verilog-AMS language, please refer to "Cadence Verilog-AMS User Manual

## Geting Start
-----------------------------------------------
### Directory structure of the Verilog-AMS source file

### Set up spectre control file
;usage
The spectre control file is used to set up corresponding simulation option. 
;Reference
For detail setup information, Virtuoso Spectre Circuit Simulator Reference
;file name 

;case illustration

### Run the simulation
;Usage

;Reference

;file name

;one case illustration


### Set up probe for visualizing signal 
;usage

;Reference

;file name

;one case illustration
For more details about AMS designer simulation, please refer to 

### Scalability
to change the scalability of the BAM neural network, you just simply change the related definition of macro xNum/yNum, For example, in the top.vams file, you can change 24 to a large scale to 96 as shown in the figure below.( 
Note that other scale also need be altered such as the test pattern dimention).

![avatar](./Image/scale.jpg) 


## License
This project is released under the Open Source License of BSD.

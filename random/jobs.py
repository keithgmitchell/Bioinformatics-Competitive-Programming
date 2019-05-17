import os


tool_name = "coral"
for i in [1, 2, 4, 8, 16, 32, 64]:
        os.system("qsub -cwd -V -N %s_%s -l h_data=10G,highp,time=1:00:00 -M $USER \
                  /u/home/k/keithgmi/project-zarlab/error.correction.benchmarking/code.evaluation/wrappers/paired_end/run.%s.sh \
                  /u/flashscratch/k/keithgmi/ec_cpu_ram/sim_rl_50_cov_%s/true_1.fastq \
                  /u/flashscratch/k/keithgmi/ec_cpu_ram/sim_rl_50_cov_%s/true_2.fastq \
                  /u/flashscratch/k/keithgmi/temp 20" % (tool_name, i, tool_name, i, i))
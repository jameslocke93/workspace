### Pre-processing  ###
#
### Methods
#	gather_data
#		Description: Reads a data file and puts the contents of that file into a data frame
#		Parameters: file_path, format
#		Output: data_frame
#
# clean_data
#		Description: Reads a data frame and removes any empty entries
#		Parameters: data_frame
#		Output:  data_frame
#
# normalise_data
#		Description: Take in a data frame and normalise each element of the data
#		Parameters: data_frame, normalisation_method
#		Output: data_frame
#
# compress_data
#		Description: Take in a data frame and remove features that have a high correlation
#		Parameters: data_frame, number_of_features (optional)
#		Output: data_frame
#######################

class Pre_processing:
	log_file="/Users/jameslocke/Documents/workspace/logs/pre_processing.log"
	config_file="/Users/jameslocke/Documents/workspace/config/pre_processing.config"

	def gather_data(self, file_path, file_format):
		pass

	def clean_data(self, data_frame):
		pass

	def normalise_data(self, data_frame, norm_method):
		pass

	def compress_data(self, data_frame, num_features=2):
		pass

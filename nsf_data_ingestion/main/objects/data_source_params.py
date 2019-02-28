import sys
import os
from nsf_data_ingestion.main.config import config

federal_reporter_param = {'FedRePORTER_PRJ_url': config.fed_FedRePORTER_PRJ_url,
                          'FedRePORTER_PRJABS_url':config.fed_FedRePORTER_PRJABS_url,
                          'hdfs_path': config.federal_hdfs_path,
                          'parquet_path': config.federal_parquet_path,
                          'directory_path': config.federal_directory_path_data}

medline_param =          {'ftp_server': config.medline_ftp_server,
                          'medleasebaseline_url':config.medline_medleasebaseline,
                          'medlease_url': config.medline_medlease,
                          'hdfs_path': config.medline_hdfs_path,
                          'xml_path': config.medline_xml_path,
                          'parquet_path': config.medline_parquet_path,
                          'directory_path': config.medline_directory_path_data,
                          'timestamp_file': config.timestamp_file}

pubmed_param =           {'ftp_server': config.pub_ftp_server,
                          'ftp_directory': config.pub_ftp_directory,
                          'download_path': config.pub_directory_path_data,
                          'unzip_path': config.pub_directory_untar_data,
                          'chunk_size': config.pub_chunk_size,
                          'chunked_path': config.pub_directory_path_processed,
                          'directory_path': config.pub_directory_path_compressed,
                          'hdfs_path': config.pub_hadoop_directory,
                          'parquet_path': config.pub_parquet_path,}

mapping =                {'federal_reporter': federal_reporter_param,
                           'medline': medline_param,
                           'pubmed': pubmed_param}
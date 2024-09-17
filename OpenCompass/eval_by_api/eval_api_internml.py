from mmengine.config import read_base
from opencompass.models.turbomind_api import TurboMindAPIModel
from opencompass.partitioners import NaivePartitioner
from opencompass.runners.local_api import LocalAPIRunner
from opencompass.tasks import OpenICLInferTask

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

with read_base():
    from ..summarizers.medium import summarizer
    from ..datasets.ceval.ceval_gen import ceval_datasets

datasets = [
    *ceval_datasets,
]

models = [
    dict(
        abbr='internlm2',
        type=TurboMindAPIModel,
        api_key='internlm2', # API key
        api_addr='http://localhost:23333/',  # Service address
        rpm_verbose=True,  # Whether to print request rate
        meta_template=api_meta_template,  # Service request template
        query_per_second=5,  # Service request rate
        max_out_len=1024,  # Maximum output length
        max_seq_len=4096,  # Maximum input length
    	run_cfg=dict(num_gpus=1, num_procs=1),
    	end_str='<eoa>',
        temperature=0.01,  # Generation temperature
        batch_size=8,  # Batch size
        retry=3,  # Number of retries
    )
]

work_dir = "outputs/api_internlm2/"

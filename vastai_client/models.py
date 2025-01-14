from dataclasses import dataclass
from typing import Dict, List, Optional
QueryType = dict[str, bool | str | list[list[str]] | dict[str, str | bool]]


@dataclass
class Instance:

    """Class for storing information about a created instance."""
    actual_status: Optional[str] = None
    bundle_id: Optional[int] = None
    bw_nvlink: Optional[float] = None
    compute_cap: Optional[int] = None
    cpu_cores: Optional[int] = None
    cpu_cores_effective: Optional[float] = None
    cpu_name: Optional[str] = None
    cpu_ram: Optional[int] = None
    cpu_util: Optional[float] = None
    cuda_max_good: Optional[float] = None
    cur_state: Optional[str] = None
    direct_port_count: Optional[int] = None
    direct_port_end: Optional[int] = None
    direct_port_start: Optional[int] = None
    disk_bw: Optional[float] = None
    disk_name: Optional[str] = None
    disk_space: Optional[float] = None
    disk_util: Optional[float] = None
    dlperf: Optional[float] = None
    dlperf_per_dphtotal: Optional[float] = None
    dph_base: Optional[float] = None
    dph_total: Optional[float] = None
    driver_version: Optional[str] = None
    duration: Optional[float] = None
    end_date: Optional[float] = None
    external: Optional[bool] = None
    extra_env: Optional[str] = None
    flops_per_dphtotal: Optional[float] = None
    geolocation: Optional[str] = None
    gpu_display_active: Optional[bool] = None
    gpu_frac: Optional[float] = None
    gpu_lanes: Optional[int] = None
    gpu_mem_bw: Optional[float] = None
    gpu_name: Optional[str] = None
    gpu_ram: Optional[int] = None
    gpu_temp: Optional[float] = None
    gpu_util: Optional[float] = None
    has_avx: Optional[int] = None
    host_id: Optional[int] = None
    host_run_time: Optional[float] = None
    hosting_type: Optional[int] = None
    id: Optional[int] = None
    image_args: Optional[List[str]] = None
    image_runtype: Optional[str] = None
    image_uuid: Optional[str] = None
    inet_down: Optional[float] = None
    inet_down_billed: Optional[float] = None
    inet_down_cost: Optional[float] = None
    inet_up: Optional[float] = None
    inet_up_billed: Optional[float] = None
    inet_up_cost: Optional[float] = None
    intended_status: Optional[str] = None
    is_bid: Optional[bool] = None
    jupyter_token: Optional[str] = None
    label: Optional[str] = None
    local_ipaddrs: Optional[str] = None
    logo: Optional[str] = None
    machine_dir_ssh_port: Optional[int] = None
    machine_id: Optional[int] = None
    mem_limit: Optional[float] = None
    mem_usage: Optional[float] = None
    min_bid: Optional[float] = None
    mobo_name: Optional[str] = None
    next_state: Optional[str] = None
    num_gpus: Optional[int] = None
    pci_gen: Optional[float] = None
    pcie_bw: Optional[float] = None
    ports: Optional[Dict[str, List[Dict[str, str]]]] = None
    public_ipaddr: Optional[str] = None
    reliability: Optional[float] = None
    rentable: Optional[bool] = None
    score: Optional[float] = None
    ssh_host: Optional[str] = None
    ssh_idx: Optional[str] = None
    ssh_port: Optional[int] = None
    start_date: Optional[float] = None
    status_msg: Optional[str] = None
    storage_cost: Optional[float] = None
    storage_total_cost: Optional[float] = None
    total_flops: Optional[float] = None
    verification: Optional[str] = None
    vmem_usage: Optional[float] = None
    webpage: Optional[str] = None


@dataclass
class Machine:

    """Class for storing information about a listed machine."""

    is_bid: Optional[bool] = None
    inet_up_billed: Optional[float] = None
    inet_down_billed: Optional[float] = None
    external: Optional[bool] = None
    webpage: Optional[str] = None
    logo: Optional[str] = None
    rentable: Optional[bool] = None
    compute_cap: Optional[int] = None
    driver_version: Optional[str] = None
    cuda_max_good: Optional[float] = None
    machine_id: Optional[int] = None
    hosting_type: Optional[int] = None
    public_ipaddr: Optional[str] = None
    geolocation: Optional[str] = None
    flops_per_dphtotal: Optional[float] = None
    dlperf_per_dphtotal: Optional[float] = None
    reliability: Optional[float] = None
    host_run_time: Optional[float] = None
    host_id: Optional[int] = None
    id: Optional[int] = None
    bundle_id: Optional[int] = None
    num_gpus: Optional[int] = None
    total_flops: Optional[float] = None
    min_bid: Optional[float] = None
    dph_base: Optional[float] = None
    dph_total: Optional[float] = None
    gpu_name: Optional[str] = None
    gpu_ram: Optional[int] = None
    gpu_display_active: Optional[bool] = None
    gpu_mem_bw: Optional[float] = None
    bw_nvlink: Optional[float] = None
    direct_port_count: Optional[int] = None
    gpu_lanes: Optional[int] = None
    pcie_bw: Optional[float] = None
    pci_gen: Optional[float] = None
    dlperf: Optional[float] = None
    cpu_name: Optional[str] = None
    mobo_name: Optional[str] = None
    cpu_ram: Optional[int] = None
    cpu_cores: Optional[int] = None
    cpu_cores_effective: Optional[float] = None
    gpu_frac: Optional[float] = None
    has_avx: Optional[int] = None
    disk_space: Optional[float] = None
    disk_name: Optional[str] = None
    disk_bw: Optional[float] = None
    inet_up: Optional[float] = None
    inet_down: Optional[float] = None
    start_date: Optional[float] = None
    end_date: Optional[float] = None
    duration: Optional[float] = None
    storage_cost: Optional[float] = None
    inet_up_cost: Optional[float] = None
    inet_down_cost: Optional[float] = None
    storage_total_cost: Optional[float] = None
    verification: Optional[str] = None
    score: Optional[float] = None
    rented: Optional[bool] = None
    bundled_results: Optional[int] = None
    pending_count: Optional[int] = None

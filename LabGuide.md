![CyberArk Logo](https://www.cyberark.com/wp-content/uploads/2024/10/cyberark-logo.svg)

# %{course_name} Instruction Manual

Welcome to the %{course_name}.  This lab environment is available for you to use 24x7 subject to the following limitations.

- Lab environment will expire after **14 days**
- Total runtime is limited to **40 hours**.
- Lab machines will shutdown after **two hours** of inactivity.

>Warning: Once the lab has expired it will be automatically deleted and cannot be recovered.

::: pagebreak :::

::: include tenantinfo.md :::

::: include SkytapTips.md :::

## Introduction
Describe the story or scenario that will play out in the lab exercises.

::: pagebreak :::

## Lab 1:  Logging into your tenant
Provide clear and concise steps to complete the lab.  It is best to use a seperate page for each step.  Give each step a level 3 (###) heading
::: pagebreak :::

### Log on to your Tenant
Browse to your tenant and log in.

|   Parameter  | Value                           |
|--------------|---------------------------------|
| **URL**      | ^^%{integration_data:app_url}^^ |
| **Username** | ^^%{integration_data:app_uid}^^ |
| **Password** | ^^%{integration_data:app_pw}^^  |

::: pagebreak :::

### Code Block Example
^^
```python
::: include md2pdf.py :::
```
^^
::: pagebreak :::

### Attachment Example
[Download the Guide](./LabGuide.pdf)

::: pagebreak :::

## What's Next?

Thank you for completing the lab, please visit our [Training Portal](https://training.cyberark.com) to explore other CyberArk training offerings. 

Feel free to use this environment as a sandbox until it expires.

<p>
	<x-command contenteditable="false" data-activate="false" data-attempts="" data-blocking="" data-command='invoke "build"' data-command-type="system" data-description="This will rerun the provisioning script and attempt to build any missing resources" data-guid="d79aa5b1-cbb2-4a88-b96c-4ef26d3f4938" data-spinner="all" data-target="%{script_vm_host}" data-timeout="0" title="This will rerun the provisioning script and attempt to build any missing resources">Reattempt Provision</x-command>
</p>
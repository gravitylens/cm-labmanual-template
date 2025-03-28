## Tenant Details
We have provisioned a tenant for you.  You will be able to access the tenant using the login details below.

### Log on to your Tenant
Browse to your tenant and log in.

| Parameter    | Value                           |
|--------------|---------------------------------|
| **URL**      | ^^%{integration_data:app_url}^^ |
| **Username** | ^^%{integration_data:app_uid}^^ |
| **Password** | ^^%{integration_data:app_pw}^^  |


warn>Warning: While this tenant is accessible from anywhere please only perform lab actions on lab machines.  Running steps on your own machine may damage your system.

If you are not seeing tenant details or have missing data click the `Reattempt Provision` button.  This will attempt to recreate any missing resources.

<p>
	<x-command contenteditable="false" data-activate="false" data-attempts="" data-blocking="" data-command='invoke "build"' data-command-type="system" data-description="This will rerun the provisioning script and attempt to build any missing resources" data-guid="d79aa5b1-cbb2-4a88-b96c-4ef26d3f4938" data-spinner="all" data-target="%{script_vm_host}" data-timeout="0" title="This will rerun the provisioning script and attempt to build any missing resources">Reattempt Provision</x-command>
</p>

::: pagebreak :::
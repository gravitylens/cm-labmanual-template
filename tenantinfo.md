## Tenant Details

We have provisioned an EPM tenant for you.  You will be able to access the tenant using the login details below.

### Verify your Tenant Details

An automated script created a tenant for you and provided the details below.  Check to see that all the values in the table have been populated.  If any are missing then something has gone wrong with the deployment.

| Parameter    | Value                           |
|--------------|---------------------------------|
| **URL**      | ^^%{metadata:app_url}^^ |
| **Username** | ^^%{metadata:app_uid}^^ |
| **Password** | ^^%{metadata:app_pw}^^  |

If everything is there, move on to the **next page**.  If you are not seeing tenant details or have missing data click the **Reattempt Provision** button below. This will attempt to recreate any missing resources.

warn>Warning: While this tenant is accessible from anywhere please only perform lab actions on lab machines.  Running steps on your own machine may damage your system.

<p>
	<x-command contenteditable="false" data-activate="false" data-attempts="" data-blocking="" data-command='invoke "build"' data-command-type="system" data-description="We have attempted to recreate any missing resources.  If you are still unable to use your tenant contact your instructor or training-labs@cyberark.com" data-guid="d79aa5b1-cbb2-4a88-b96c-4ef26d3f4938" data-spinner="all" data-target="%{script_vm_host}" data-timeout="0" title="Reattempt Provisioning">Reattempt Provision</x-command>
</p>

::: pagebreak :::
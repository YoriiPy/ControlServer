import asyncio

async def restart_server():
    process = await asyncio.create_subprocess_shell(cmd="reboot", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()

    stdout_str = stdout.decode().strip()
    stderr_str = stderr.decode().strip()
    return {
        "returncode": process.returncode,
        "stdout": stdout_str,
        "stderr": stderr_str
    }


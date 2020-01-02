wrk.method = "GET"
wrk.headers["Content-Type"] = "application/json"
done = function(summary, latency, requests)   
   io.write("------------------------------\n")
   for _, p in pairs({ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 99, 99.999 }) do
      n = latency:percentile(p)
      io.write(string.format("%g%%,%d\n", p, n))
   end
end
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/contact" && request.method === "POST") {
      const reply = (status, ok) => Response.json({ ok }, { status });
      if (!env.LEADS) return reply(503, false);
      const origin = request.headers.get("origin");
      if (origin && origin !== url.origin) return reply(403, false);
      if (+(request.headers.get("content-length") || 0) > 8000) return reply(413, false);
      let d;
      try { d = await request.json(); } catch { return reply(400, false); }
      if (d?.website) return reply(200, true);
      const s = (v, n) => (typeof v === "string" ? v.trim().slice(0, n) : "");
      const lead = {
        name: s(d?.name, 80),
        phone: s(d?.phone, 20),
        product: s(d?.product, 60),
        message: s(d?.message, 1000),
        at: new Date().toISOString(),
      };
      if (lead.name.length < 2 || !/^(\+98|0098|0)9\d{9}$/.test(lead.phone)) return reply(422, false);
      await env.LEADS.put(`lead:${lead.at}:${crypto.randomUUID()}`, JSON.stringify(lead));
      return reply(200, true);
    }
    return env.ASSETS.fetch(request);
  },
};

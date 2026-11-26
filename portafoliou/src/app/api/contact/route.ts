import { NextResponse } from "next/server";
import { Resend } from "resend";

export async function POST(request: Request) {
  try {
    const apiKey = process.env.RESEND_API_KEY;
    const contactEmail = process.env.CONTACT_EMAIL;

    if (!apiKey || !contactEmail) {
      return NextResponse.json(
        {
          success: false,
          message: "El servicio de contacto no está configurado.",
        },
        { status: 503 }
      );
    }

    const resend = new Resend(apiKey);
    const body = await request.json();

    const name = String(body.name ?? "").trim();
    const email = String(body.email ?? "").trim();
    const message = String(body.message ?? "").trim();

    if (!name || !email || !message) {
      return NextResponse.json(
        {
          success: false,
          message: "Todos los campos son obligatorios.",
        },
        { status: 400 }
      );
    }

    const emailRegex =
      /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailRegex.test(email)) {
      return NextResponse.json(
        {
          success: false,
          message: "El correo electrónico no es válido.",
        },
        { status: 400 }
      );
    }

    if (name.length > 100) {
      return NextResponse.json(
        {
          success: false,
          message: "El nombre es demasiado largo.",
        },
        { status: 400 }
      );
    }

    if (message.length > 5000) {
      return NextResponse.json(
        {
          success: false,
          message: "El mensaje es demasiado largo.",
        },
        { status: 400 }
      );
    }

    await resend.emails.send({
      from: "Portafolio <onboarding@resend.dev>",
      to: [contactEmail],
      subject: `Nuevo mensaje de ${name}`,
      replyTo: email,
      text: `
Nombre: ${name}

Correo: ${email}

Mensaje:

${message}
      `,
    });

    return NextResponse.json({
      success: true,
      message: "Mensaje enviado correctamente.",
    });
  } catch (error) {
    console.error("Error en /api/contact:", error);

    return NextResponse.json(
      {
        success: false,
        message: "No fue posible enviar el mensaje.",
      },
      { status: 500 }
    );
  }
}